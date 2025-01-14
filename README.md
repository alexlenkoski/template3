# Python template project

This repository is meant to be a starting point for project work in Python. We have [another repository](https://github.com/NorskRegnesentral/python_project_standard/tree/main), that serves more as an introduction to project work in Python and contains a lot of useful information. If you are wondering about something Python-related, you could try to check that out.

<!-- START 'Markdown All in One generated TOC -->
**Table of Contents**
- [Python template project](#python-template-project)
  - [Introduction](#introduction)
  - [How to create a package?](#how-to-create-a-package)
    - [Steps to creating your own package](#steps-to-creating-your-own-package)
    - [Poetry - a Python package manager](#poetry---a-python-package-manager)
      - [Installing Poetry](#installing-poetry)
    - [Package setup](#package-setup)
    - [Package dependencies](#package-dependencies)
      - [Installing package from Github using Poetry](#installing-package-from-github-using-poetry)
      - [Installing package from Github using pip](#installing-package-from-github-using-pip)
      - [Installing package from local folder](#installing-package-from-local-folder)
    - [Running unit tests](#running-unit-tests)
    - [Poetry configuration files](#poetry-configuration-files)
    - [Virtual environments and python versions](#virtual-environments-and-python-versions)
  - [Building a python package](#building-a-python-package)
    - [Publishing a package to PyPi (public server)](#publishing-a-package-to-pypi-public-server)
  - [Semantic versioning of software](#semantic-versioning-of-software)
    - [Using poetry and git for semantic versioning](#using-poetry-and-git-for-semantic-versioning)

<!-- END 'Markdown All in One' generated TOC -->


## Introduction
The intended use of this repository is as a template for when you're creating a new python project repo in Github. As such, instead of cloning down this repo directly,
you should instead create a new repo in Github, and then choose this repo as the template for that. Alternatively, on GitHub you can press the **"Use this template"** button in the upper right corner of the window.

With this template for Python projects, we will attempt to provide a template that is easy to work with and provides sufficient functionality for most projects.
We give a recipe for how to setup your Python project and installing it. This template is based on the use of 'virtual environments' to keep our
required python packages installed separately from the rest of your operating system. And to do this job as well as several other package-related tasks,
we suggest to use the tool `poetry`.
In addition, we've set up a way to integrate tests that checks your code when it's pushed to Github.

If you wish to see an example of a more fully fledged example python project, you can check out [python_project_standard](https://github.com/NorskRegnesentral/python_project_standard).
There we've included more information on how to setup a python development environment in VS Code, as well as examples of interactive scripts and functions implemented in different
files and sub-folders of the main project package.

## How to create a package?
The layout of this project repository is as follows.
```
.
├── LICENCE.txt
├── notebooks
│   └── example_notebook.ipynb
├── scripts
│   └── example_script.py
├── poetry.toml
├── pyproject.toml
├── README.md
├── src
│   └── package_name
│       └── __init__.py
│
└── tests
    └── test_example.py

```
We will start by the most important directory in this repository, which is the "src"-folder. All the code within the package you are building should be placed within the "src"-folder. The "src"-folder separated the source code of your package from other scripts such as tests, documentations and notebooks/scripts with examples of how the package can be used. The directory "package_name" in the "src" folder, contains the package that is made. In order for Python to know that `package_name` is a module, and not only a directory, it must contain a file named "\_\_init\_\_.py". The \_\_init\_\_.py-file can be empty, but signals to Python that the directory is also a module which allows importation of the directory and sub-modules within the directory that otherwise would not be possible.


### Steps to creating your own package
1. Change the name of the directory "package_name" inside the "src"-folder to the name of the package you are developing.
2. In the "pyproject.toml"-file, the following changes must made:

    a) The information about the package, such as the name of the package, its author(s), the version of the package and so forth must be specified in the top of the file beneath the `[poetry.tool]`-header.

    b) Dependencies of the package are included below the `[tool.poetry.dependencies]` header. Here, you can also specify which Python versions the package is compatible with. This can also be left empty, and our package manager `poetry` will update it when new packages are added, more on this later.

    c) *Optional*. When developing and using the package, it can be useful to provided examples of how the package can be used. This could e.g. entail running unit tests, or plotting some results of the package which would require the use of a library like `matplotlib`. This means that there are packages that are required in development that are not a dependency of the package. Such development dependencies are specified below the header `[tool.poetry.group.dev.dependencies]`, and can again be added using the poetry tool as explained below.

If the above changes have been made, you are ready to install the package and start developing it. In order to do that, we will introduce you to a package manager called "poetry" in the following sections.

### Poetry - a Python package manager
In order to ensure that it's easy to get going on a project which uses a certain set of packages, we're recommending the use of a tool called
Poetry. This tool makes it relatively easy to add packages you need for your project, and also bundle up your package and either send it to someone else, or publish it online so that others can use it.

In this README we're mostly assuming that you're using the `bash` terminal on Linux or `PowerShell` on Windows.
The required commands and configuration are likely to change if that's not the case.
There is however some support for setting the correct $PATH variable and another environment
variable required for working over SSH using a `tcsh` shell.

#### Installing Poetry
To install poetry, we recommend using a tool called `pipx`, which will install Poetry itself in a contained environment where it does not
interfere with any of your other installed python packages. To this end, we assume that you have the regular python package installer
`pip` available.

If that is the case, you can run the following commands in your terminal to install `poetry`:

(On windows, you might have to replace 'python3' with 'python' or 'py', depending on how you installed python.)

- First we install the 'pipx' tool to our 'user' package directory:
  - `python3 -m pip install --user pipx`.

- Then we use `pipx` to install `poetry` at a given version:
  - `python3 -m pipx install poetry==1.6.1`.

  - This command will likely output some warnings telling you that programs where installed into one or two directories
  "that are not on the `$PATH` variable". This variable is a list of directories stored as a (semi-)colon separated string
  that the operating system searches through to find a program name when we type it into the terminal. It is helpful to copy
  down these directories and saving them in a text file for reference later if we need to add them to the `$PATH` variable manually.

  - When the directories containing our python programs are not in the `$PATH` variable, the operating system will not find either `pipx` or `poetry`
  when we try to call them from the terminal. In the next point we will attempt to fix that, first automatically
  using `pipx` itself, and if that does not work then we'll try the more manual route. Regardless of wether or not we add these directories to
  the `$PATH` variable, you should be able to call `pipx` and `poetry` using the `python3 -m <poetry|pipx> [cmd]` syntax.

- To attempt to add the required folders containing our python programs into the `$PATH` variable,
  we use the `ensurepath` command of `pipx`:
  - `python3 -m pipx ensurepath`.
  - If this does not work, we have to manually add the directories where 'pipx' and 'poetry' have been installed
    to our `$PATH` variable. This process is different for Linux and Windows.
  - On a Windows laptop:
    - In a Powershell terminal window, we first find our `$PROFILE` file, which is executed when Powershell starts whenever it exists. We can find
      this by running `echo $PROFILE`.
    - Open this file by running `notepad $PROFILE`. If you get a promt saying that the file does not exist, confirm that you want to create it.
    - In the notepad window, add the directories that pipx warned about earlier as missing from the `$PATH` with this
      command: $Env:PATH += ";\<python-program-directory\>"
    - In my case I added the following two lines:
      - $Env:PATH += ";C:\Users\jvkolsto\\.local\bin\"
      - $Env:PATH += ";C:\Users\jvkolsto\AppData\Local\Programs\Python\Python311\Scripts\"
  - On a (Linux) server:
    - To add the path `~/.local/bin` to your `$PATH` on the servers, run one of the following commands in a shell:
    - Linux `bash` shell (Each line starting something like: `<username>@NR-F0YBHW3:~ $`):
      - `echo -e "\n# Add ~/.local/bin to PATH for python-apps like poetry:\nexport PATH=\"\$PATH:$(echo ~)/.local/bin\"\n" >> ~/.bashrc`
    - Linux `tcsh` shell (Each line starting something like: `NR-F0YBHW3:~>`):
      - ``echo "\n# Add ~/.local/bin to PATH for python-apps like poetry:\nsetenv PATH "\"\$PATH\"":`echo ~`/.local/bin\n" >> ~/.tcshrc``
    - The above commands append a few lines of text to your `~/.bashrc` or `~/.tcshrc` file, which is like the `$PROFILE` file for
      Powershell, in the sense that your shell runs all the commands in this file every time it starts.
    - If you need to add other paths, use a terminal text editor (e.g. nano, pico or vim) and open the corresponding configuration
      file. Then you can copy the previous line that was pasted to the end of the file and switch out which folder that's
      appended to the `$PATH` variable.

- Lastly: When working over SSH onto e.g. the SAMBA servers, we need to set a variable that informs `poetry` not to check for
          any other package repository except for the standard one. 
          Run one of the following commands from your shell on a server:
  - Linux bash shell (Each line starting something like: `<username>@NR-F0YBHW3:~ $`):
    - `echo -e "\n# Added to fix poetry over SSH:\nexport PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring" >> ~/.bashrc`
    - then either run `source ~/.bashrc` or start another terminal where you can begin using `poetry`.
  - Linux tcsh shell (Each line starting something like: `NR-F0YBHW3:~>`):
    - `echo "\n# Added to fix poetry over ssh:\nsetenv PYTHON_KEYRING_BACKEND keyring.backends.null.Keyring" >> ~/.tcshrc`
    - then either run `source ~/.tcshrc` or start another terminal where you can begin using `poetry`.


### Package setup
We've set up the `pyproject.toml` file to install the local `<package_name>` into the project dependency. And all code changes done within
`src/<package_name>` will be reflected the next time you start python. To install the python virtual environment you run
- `poetry install`

from the top level repo-directory (the folder you cloned the repo into). And then if you want to update all you packages to their newest compatible versions, you run
- `poetry update`.

If you only want to update a specific pacakge, you instead run 
- `poetry update <package-name>`


### Package dependencies
When you want to add or remove a package from your project's python installation, you use
the `poetry `commands `add` and `remove` followed by the name of the package. For example,
you could do:
- `poetry add numpy`
- `poetry remove scipy`

To specify a version for the package to install, one uses this syntax:
- `poetry add numpy@1.26.3`

And then if you wish to revert to the latest version, you can do:
- `poetry add numpy@latest`

And if you want to include a package that you only need when you're developing the package or
working interactively,you can specify the group that a package belongs under like this:
- `poetry add <package> --group dev`
We have already added some pacakges under the `dev` group, to facilitate unit testing,
running jupyter notebooks, and linting/formatting of python code.

#### Installing package from Github using Poetry
In order to add a package dependency from a Github repository (that you have read access to), you
first go to the repository and copy the SSH-url. This is the string you would usually copy to clone
down the repository yourself through the command `git clone <git-ssh-url>`.
An example github ssh URL for the package ERApy is 
`git@github.com:SeasonalForecastingEngine/ERApy.git`.
Then we run a poetry command to install that package from Github:

- `poetry add --editable git+ssh://git@github.com:SeasonalForecastingEngine/ERApy.git`

This command will build and install the python package ERApy from the default branch,
usually `main` or `master`, and the `--editable` argument tells poetry to grab the newest
version of the repo whenever you do `poetry update`. 
If you want to specify a specific branch og tag to install from, you can add a signifier 
`#<tag-or-branch>` to the end of the Github SSH URL, resulting in the following command:

- `poetry add git+ssh://git@github.com:SeasonalForecastingEngine/ERApy.git#<tag-or-branch>`

In the above example command I've removed the `--editable` argument. At least when installing
specific version of a package from Github as specified by a tag (i.e. `v0.1.3`) the code for that 
version should not change, and therefore it makes less sense to grab the "latest" version of the 
package from Github each time we run `poetry update`.  

#### Installing package from Github using pip
It is also possible to install a package from Github using pip, if for example a 
customer does not use poetry, but then we need to slightly modify the Github SSH URL.
Specifically, we replace the `:` after 'github.com' with a `/` in the URL. As an example,
to install ERApy from Github using pip, we'd run this command:

- `pip install git+ssh://git@github.com/SeasonalForecastingEngine/ERApy.git`

#### Installing package from local folder
Say you're working on two different packages at the same time, and the second package
uses the first one as a dependency. Then it might be useful to use the development 
version of the first package in your second package as you're developing both packages. 

We can achieve this by using poetry to add a package directly from a folder on your local 
machine. Say the ERApy package is stored in the same folder as the second package 
we're working on. To install ERApy then, we could use the command
- `poetry add ..\ERApy\ --group dev`

where I've added to argument to group ERApy under development dependencies, to show that
this is possible as well in this context.


### Running unit tests
When building a package it can be helpful to write tests to check that
the functionality is as expected. One tool to do this for python-packages
is called `pytest`, and we've added this tool as a development dependency
in this python project template.

Tests are defined by function with names starting with `test_`, in python files starting with 'test_' under the 'tests/' folder. There are example
tests already present that showcase some of the functionality of `pytest`.

To run these tests, we invoke `pytest` through `poetry`, which ensures that
pytest runs under the virtual environment managed by `poetry`.
- `poetry run pytest`
And this produces a test-summary in the terminal showing wether or not tests passed.

### Poetry configuration files
This section is more for the people that are especially interested in how `poetry` works, and can probably be skipped on
a first reading.

Essentially the idea is that all the configuration needed to specify the dependencies and tooling required for a
python package should be specified in the `pyproject.toml` file. This file contains the headers `[tool.poetry]`,
`[tool.poetry.dependencies]` and several others, and different tools use the lines under each header to specify
how they work. We've already added a 'template' poetry project configuration at the top of this file, but this
needs to be changed before you start using this package template yourself.

Inside this `pyproject.toml` file we've also added configuration that make it easy to make and run tests
on the functionality of your package. This is under the `[tool.pytest.ini_options]`. And yet another useful tool
for minimizing small typos and errors in your python code is the `ruff` package, which you'll find configured under
the `[tool.ruff]` and `[tool.ruff.format]` headers.

Now while the `pyproject.toml` contains the list of the packages that you want available in your python project,
those packages might again depend on other packages, and so on. Therefore, to save a reproducible *snapshot* of
your python project/virtual environment, `poetry` generates the file `poetry.lock`. This file is machine generated,
and not meant for human consumption. However, if there is such a file in your repository when you run
`poetry install`, you should in principle get the exact same set of packages as another developer.

Lastly, the `poetry.toml` file contains configuration specific to the `poetry` tool. Here we've set the options
such that `poetry` generates the virtual environment within the repo-directory. And such that the cache directory
used by `poetry` is also within the repo-directory. In this way the entire python project becomes quite well
contained within the repository.

### Virtual environments and python versions

When working with Python, it can often be necessary to use different versions of packages in different projects, and it is also important to maintain dependencies between packages. For reproducibility, it is important to keep track of which package versions are used within a project. In order to achieve this, and more, it can be useful to work with a **virtual environment**. A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated spaces for them. This is particularly useful when different projects require different versions of the same package or dependency.

A virtual environment is a tool that helps to keep dependencies required by 
different projects separate by creating isolated spaces for them. This is particularly useful when different projects require different versions of the same package or dependency.

In the context of Python, a virtual environment (often abbreviated as "venv") is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages. When you create a virtual environment, a fresh Python binary is installed along with a copy of the pip installer.

By activating a virtual environment, you can work with specific versions of Python and installed packages without affecting other projects that might be using different versions. This allows for a much cleaner and more manageable development environment. It can be useful to have a separate virtual environment for each Python project you are working on.
And with `poetry` installed, the easiest way to activate the project virtual environment is to run `poetry shell`.

To sum it up, virtual environments provide a way to avoid conflicts between system-wide packages and project-specific packages,
and to ensure reproducibility and reliability of software projects.

When a poetry package is initialized, a virtual environment is created, and it's by default put in the `.venv/` folder.


## Building a python package
When we want to distribute a package, we build / bundle up the code using this command:
- `poetry build`

which should give a similiar output to this:
```
Building package_name (0.1.0)
  - Building sdist
  - Built package_name-0.1.0.tar.gz
  - Building wheel
  - Built package_name-0.1.0-py3-none-any.whl
```
The resulting files `package_name-0.1.0.tar.gz` and `package_name-0.1.0-py3-none-any.whl` are placed in the `dist/` folder. They are, respectively,
the `sdist` and `wheel` distribution formats. We recommend using the wheel 
distribution formats as the standard file to share to consumers of your package.

For users of your python package that have received a wheel (`example_pkg.whl`) file, they can install the package in they environment by running 
- `poetry add example_pkh.whl`

And any dependencies specified for your package will be automatically installed as well. 

It is not necessary to know all the 
differences between these two formats, but at a course level the `sdist` format 
is a "source distribution" which leaves it up to the people that install the 
package to compile any source code in e.g. `c++`, `fortran`, or `rust`.
The wheel format on the other hand moves the compilation work to the 
person building the package (i.e. us). This should hopefully make for an easier
installation process for the end user, and should decrease installation times.

### Publishing a package to PyPi (public server)
If you want to publish your python package to the public such that everyone can install your package through `pip`, we need to publish to the Python Package Index (PyPi).
There is a good tutorial on how to do this [here](https://www.digitalocean.com/community/tutorials/how-to-publish-python-packages-to-pypi-using-poetry-on-ubuntu-22-04).

There are essentially three steps to the procedure.
1. Make an account on `pypi.org`
2. Generate an API-token and configure poetry to use this API-token.
3. Run `poetry build` and `poetry publish`

If all goes well and the name of your package does not conflicts with any existing packages (this might we wortwhile to check out beforehand), you should be able 
to install your package from anywhere using `poetry add <package_name>` or `pip install <package_name>`. Administration of your package happens on the PyPi website.

## Semantic versioning of software
When we start releasing software packages that are used both internally and by clients, it is important that we as developers follow 
versioning rules to ensure traceability and consistency for the users of our software. One common versioning scheme is called 
**semantic versioning**, and it's ethos can be found [here](https://semver.org/).

In essence, semantic versioning consists of using 
three digits to signify the version of a software package.
The format is `MAJOR.MINOR.PATCH`, so the version string `2.3.11` indicates 
a major version of 2, minor version 3, and patch version 11.

In this template, the semantic version starts at `0.1.0`. And the idea is that wenever a small 
change (i.e. a "patch") is added, but which does not introduce any new functionalioty, we bump the patch version. That is, `0.1.0 => 0.1.1`. 

Now if we introduce new functionality without breaking any old usage
of our package (keeping the same API), we bump the minor version number and reset the patch number.
That is, `0.1.1 => 0.2.0`. 

Lastly, if we introduce changes that break or remove functionality, we bump the major version number,
and reset both minor and patch versions. That is, `0.2.0 => 1.0.0`. 
This way, users of our package should be able to stay on a 
given major version number, and expect that the functionality they're using keeps working even if they
update to newer minor versions or patches.

### Using poetry and git for semantic versioning
To integrate the semantic versioning scheme into our workflow, we need a way to store the package version
along with our source code, and a way to inform git which commit (source code snapshot) corresponds 
to a given semantic version.

In these python projects, we store the package version in the `pyproject.toml` file, under the `[tool.poetry]`
header in the `version` variable. When we wish to change this version number after making changes to our
source code we can either do it manually, or let poetry help us.

If we run the command `poetry version` in the terminal, we'll get back an output signifying the current
version of our package. And then if we want to bump (increment) the patch version number, we can 
run `poetry version patch`, and then poetry will modify the correct field in the `pyproject.toml` file
and print out the new version number to the terminal.
To bump either the minor or major version number you can equivalently do `poetry version <minor|major>`.
And lastly, if you want to specify a specific version string, you can also do `poetry version 0.1.0-rc1` 
or any other version string that you like.

Then after you've made the changes to the package version, you make a commit with the new version number,
hopefully with a commit message which explains the changes made. And after making that commit, we wish to 
inform git that the state of our repo at this moment represent the newest version we just bumped to.
The way to do that is through a **git tag**. In a sense a tag is just a commit with a human readable name
in addition to the machine generated hash which uniquely identifies each commit.

The way to add a tag to the most recent commit which bumped the version to `1.0.4` using git,
is to run the command:
- `git tag -a v1.0.4 -m "Bumped version to 1.0.4"`

Lastly, we need to push the tag we just made to Github. Tags are not pushed when running the usual 
`git push`, and instead we have to explicitly state which tag we want to push to Github. In the current
example where we added the tag `v1.0.4`, we would push the new tag to Github with the following command:
- `git push origin tag v1.0.4`

The `v` in front of the semantic version `1.0.4` is simply there as a convention for signifying that this tag
indicates a semantic version number. And then later, if we wish to check out the state of our package at
a certain version, we could do:
- `git checkout v1.0.4`

and then we'd be looking at the source code as it was for version `1.0.4`.
