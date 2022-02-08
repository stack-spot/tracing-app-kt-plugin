from os import remove
from pathlib import Path
from typing import List
from unittest import result

from templateframework.metadata import Metadata
from templateframework.runner import run
from templateframework.template import Template


def read_dockerfile(dockerfile_path: Path):
    with dockerfile_path.open() as dockerfile:
        return dockerfile.readlines()

def configs_before_tag_from_in_dockerfile(dockerfile_configs: List[str]):
    configs_before_tag_from = []
    for line in dockerfile_configs:
        if not line.startswith('FROM'):
            configs_before_tag_from.append(line)
        else:
            break
    return configs_before_tag_from

def remove_configs_before_tag_from(dockerfile_configs: List[str], configs_before_tag_from: List[str]):
    for line in configs_before_tag_from:
        dockerfile_configs.remove(line)
    return dockerfile_configs

def create_new_dockerfile_list(current_dockerfile_configs: List[str], configs_before_tag_from: List[str]):
    return current_dockerfile_configs + configs_before_tag_from

def write_in_dockerfile(dockerfile_path: Path, final_dockerfile_configs: List[str]):
    with dockerfile_path.open('w') as dockerfile_to_write:
        for line in final_dockerfile_configs:
            dockerfile_to_write.write(line)

def move_tag_entrypoint_to_last_line(new_dockerfile_configs: List[str]):
    entrypoint = ''
    for line in new_dockerfile_configs:
        if line.startswith('ENTRYPOINT'):
            entrypoint = line
            break
            
    if entrypoint != '':
        new_dockerfile_configs.remove(entrypoint)
        new_dockerfile_configs.append(entrypoint)
    return new_dockerfile_configs

def delete_empty_file(path: Path):
    if path.is_file() and path.stat().st_size == 0:
        path.unlink()

class PutDockerfileSetthingsInTheRightPlace(Template):
    def post_hook(self, metadata: Metadata):
        resource_path = metadata.target_path.joinpath('app')
        dockerfile_path = resource_path.joinpath('Dockerfile')
        config_file_path = resource_path.joinpath('config.yaml')
        
        dockerfile_configs = read_dockerfile(dockerfile_path)
        configs_before_tag_from = configs_before_tag_from_in_dockerfile(dockerfile_configs)
        current_dockerfile_configs = remove_configs_before_tag_from(dockerfile_configs, configs_before_tag_from)
        new_dockerfile_configs = create_new_dockerfile_list(current_dockerfile_configs, configs_before_tag_from)
        final_dockerfile_configs = move_tag_entrypoint_to_last_line(new_dockerfile_configs)
        write_in_dockerfile(dockerfile_path, final_dockerfile_configs)
        delete_empty_file(config_file_path)

if __name__ == '__main__':
    run(PutDockerfileSetthingsInTheRightPlace())