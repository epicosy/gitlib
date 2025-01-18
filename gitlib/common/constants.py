# captures pull requests and diffs
HOST_OWNER_REPO_REGEX = (r'(?P<host>(git@|https:\/\/)([\w\.@]+)(\/|:))(?P<owner>[\w,\-,\_]+)\/(?P<repo>[\w,\-,\_]+)'
                         r'(.git){0,1}((\/){0,1})')

# capture commit reference
COMMIT_REF_REGEX = r'(github|bitbucket|gitlab|git).*(/commit/|/commits/)'

# capture the commit sha
COMMIT_SHA_REGEX = r'\b[0-9a-f]{5,40}\b'

DEFAULT_FILENAMES_TO_SKIP = ('test', )
