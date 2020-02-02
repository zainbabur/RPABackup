# RPABackup
At work many of our files are updated by UiPath, an RPA tool. The data in those files is necessary for daily operations and thus need to be updated on time. Anyone who has used UiPath or any other RPA tool knows that sometimes it just fails (e.g. due to an unexpected popup which blocks a UI element, or unexpected time delays, etc.).\
We were forced to check the data manually to ensure that it was up to date, which interfered with other tasks and projects, so I wrote this simple script.
It is scheduled to run every three hours, and checks the modified times of the files.
If any of the files is not updated within the last 'delta' hours, it starts the coresponding RPA through batch files.
Future upgrades will include email alerts as well.
