# Git command-line wrappers

import os
import subprocess

class NoCurrentBranchError(Exception):
    pass

def _git(*args):
    '''Run a git command and return a list of lines'''
    cmd = subprocess.Popen(['git'] + list(args), stdout=subprocess.PIPE)
    return cmd.communicate()[0].split(os.linesep)[:-1]

def get_current_branch():
    for line in _git('branch', '--no-color'):
        if '*' in line:
            return line.split()[1]
    raise NoCurrentBranchError

def get_tags(pattern=None):
    if pattern:
        return _git('tag', '-l', pattern)
    else:
        return _git('tag')

def get_tag_message(tag):
    message = []
    for line in _git('show', '--raw', '--no-color', tag)[4:]:
        if line.startswith('commit '):
            message.pop()
            return message
        message.append(line)
    raise Exception('Failed to get tag message')

def log(revlist):
    return _git('log', '--no-color', '--oneline', revlist)

def tag(name, annotate=None):
    if annotate:
        _git('tag', '-a', '-F', annotate, name)
    else:
        _git('tag', name)

def format_patch(revlist, subject_prefix=None, output_directory=None, numbered=False, cover_letter=False):
    args = ['format-patch']
    if subject_prefix:
        args += ['--subject-prefix', subject_prefix]
    if output_directory:
        args += ['--output-directory', output_directory]
    if numbered:
        args += ['--numbered']
    if cover_letter:
        args += ['--cover-letter']
    args += [revlist]
    _git(*args)

def send_email(to_list, cc_list, revlist_or_path):
    args = ['git', 'send-email']
    for address in to_list:
        args += ['--to', address]
    for address in cc_list:
        args += ['--cc', address]
    args += [revlist_or_path]
    subprocess.call(args)
