import logging
import os.path
import shutil
import tarfile
import tempfile
import time

import requests

from objects.repo_data import RepositoryData
from services.externalrepo.external_repo_service import ExternalRepoService

logger = logging.getLogger(__name__)

TARBALL_PATH = 'https://api.github.com/repos/'


class GitHubService(ExternalRepoService):

    def fetch_repository(self, repo_data: RepositoryData) -> str:
        tarball_path = f'https://api.github.com/repos/{repo_data.get_repo_path()}/tarball/{repo_data.get_repo_ref()}'
        headers = {
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28'
        }
        if repo_data.get_access_token():
            headers['Authorization'] = f'Bearer {repo_data.get_access_token()}'
        sys_temp_fir = tempfile.gettempdir()
        temp_dir = os.path.join(sys_temp_fir, f'repo_{repo_data.get_transformation_id()}')
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        os.makedirs(temp_dir, exist_ok=True)
        tar_file = os.path.join(temp_dir, 'repo_tarball.tar.gz')
        for retry in range(5):
            response = requests.get(tarball_path, headers=headers, stream=True)
            if response.status_code == 200:
                with open(tar_file, 'wb') as file:
                    shutil.copyfileobj(response.raw, file)
            else:
                time.sleep(0.5)
                continue

            with tarfile.open(tar_file, 'r:*') as tar:
                tar.extractall(path=temp_dir)

            dir_items = os.listdir(temp_dir)
            for dir_item in dir_items:
                if dir_item != 'repo_tarball.tar.gz':
                    return os.path.join(temp_dir, dir_item)

        raise Exception(f'unable to fetch repository: {repo_data.get_repo_path()}/{repo_data.get_repo_ref()}')

    def clean_up_repository(self, repo_path) -> None:
        abs_path = os.path.abspath(repo_path)
        parent_dir = os.path.dirname(abs_path)
        shutil.rmtree(parent_dir, ignore_errors=True)
