import requests

from github.File import File
from gitlib.models.diff.patch import Patch
from gitlib.parsers.patch.git import GitPatchParser
from gitlib.parsers.patch.unified import UnifiedPatchParser


class GitFile:
    def __init__(self, file: File):
        self.file = file
        self._content = None

    @property
    def content(self) -> str:
        if self._content is None:
            self._content = requests.get(self.file.raw_url).text

        return self._content

    def get_patch(self, old_file=None) -> Patch:
        # TODO: find a way to compute the patch from the raw content of current and previous versions
        if old_file:
            assert isinstance(old_file, GitFile)
            parser = UnifiedPatchParser(self.content, old_file.content, self.file.filename, old_file.file.filename)
        else:
            parser = GitPatchParser(self.file.patch, self.file.filename, self.file.previous_filename)

        return parser()
