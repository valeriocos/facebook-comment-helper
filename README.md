# facebook-comment-helper
A tool that helps community managers to find and answer relevant comments in their FB pages

## Licensing
The tool is distributed under the MIT License (https://opensource.org/licenses/MIT)

## Technical details
- Windows 7
- Python 2.7.6

## Installation and Execution
The tool can be installed using the setup.py or as Windows program.

Command line:
```
C:\facebook-comment-helper> python setup.py install
C:\facebook-comment-helper> python ./gui/comment_helper_gui.py
```

Windows program:

After executing the setup (see [installation](tree/master/installation) folder), 
the tool will be saved in the machine (default location C:\Program Files\FacebookCommentHelper) and a shortcut will be created on the Desktop

Note that the installation has been created for Windows 7 64-bit. To build other installation, see section **Build your own installation** 

## How to
The tool comes with a simple GUI that needs a Facebook token and a target page.

Then, by clicking on the button "Launch Browser", a Chrome browser will open and point to facebook.com 
to allow the user to log in.

Once the user is logged in, he can click the "Get Next Comment" button. The tool will look for the next 
**relevant comment*** and show it in the browser. At that moment, the user will be able to answear/react to the comment.

At any moment the user can close the tool by clicking on the exit button of the GUI.

**Note that a relevant comment is a comment that contains a photo or a video*

## Limitations
Currently the tool does not look for relevant comments in nested comment replies.

## Tutorial
A short tutorial showing how to use the tool is available in the [docs](tree/master/docs) folder

## Build your own installation
In order to build your own installation, you need:

- WinPython (https://winpython.github.io/), which is a portable distribution of Python
- Inno Setup (http://www.jrsoftware.org/isinfo.php), which generates installer for Windows programs.

### Process:



