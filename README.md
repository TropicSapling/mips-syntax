mips-syntax
===========

MIPS syntax highlighting package for [Sublime Text](https://www.sublimetext.com/) (versions 2-4).


For users
---------

#### Recommended
1. Install [PackageControl](https://packagecontrol.io/).
2. Open the command palette (default keybinding: `Ctrl+Shift+P`), select `Package Control: Install Package` and choose `MIPS Syntax`.
3. Download all files and move them into `Packages/MIPS Syntax/` (create folder if it doesn't exist). This step is needed to get the changes from this fork, which are not included in the installed package.
    - Linux full path: `~/.config/sublime-text-<VERSION>/Packages/MIPS Syntax/`
    - Windows full path: `C:\Users\<USER>\AppData\Roaming\Sublime Text <VERSION>\Packages\MIPS Syntax`

#### Manual
Click on "Download ZIP", extract the archive into sublime's package folder, e.g. `~/.config/sublime-text-3/Packages/User/`.


For developers
--------------

If you want to change something, you can do that just by editing the files, but you can also install AAAPackageDev for sublime and then:

* edit `mips.JSON-tmLanguage`
* run *build* in Sublime and select *Convert to: Property List*
* increment version number in `packages.json`

In order to test your changes, you can symlink the repository to sublime's package folder, e.g.

    $ ln -s /tmp/mips-syntax/ ~/.config/sublime-text-3/Packages/User/


Feel free to send merge requests!
