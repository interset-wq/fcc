# Working with Code Editors and IDEs

In these lectures, you will learn how to work with code editors and IDEs. You will learn various concepts about the most popular code editor, VS Code such as its installation, how to create a project in it, keyboard shortcuts, and extensions.

## What Is a Code Editor and IDE?

You might think these are the same thing, but not quite. A code editor is any application that allows you to edit code files. An IDE, or Integrated Development Environment, is a full application that allows you to compile, run, and debug your code while you edit it.

您可能认为这些是一回事，但不完全是。代码编辑器是允许您编辑代码文件的任何应用程序。IDE（即集成开发环境）是一个完整的应用程序，允许您在编辑代码时编译、运行和调试代码。

Perhaps some examples might be helpful.

也许一些例子可能会有所帮助。

First, let's consider a few popular IDEs. Visual Studio is an integrated development environment by Microsoft that provides a comprehensive suite of tools for building, debugging, and deploying applications across various platforms.

首先，让我们考虑一些流行的 IDE。Visual Studio 是 Microsoft 的集成开发环境，它提供了一套全面的工具，用于跨各种平台构建、调试和部署应用程序。

Another IDE is XCode. Xcode is an integrated development environment by Apple designed for creating, coding, and debugging applications for macOS, iOS, watchOS, and tvOS.

另一个 IDE 是 XCode。Xcode 是 Apple 的集成开发环境，旨在为 macOS、iOS、watchOS 和 tvOS 创建、编码和调试应用程序。

And another IDE would be Android Studio. Android Studio is an integrated development environment by Google specifically designed for building, debugging, and testing Android applications.

另一个 IDE 是 Android Studio。Android Studio 是 Google 专门为构建、调试和测试 Android 应用程序而设计的集成开发环境。

Those are just a few examples of IDEs. Now, let's take a look at a few popular code editors.

这些只是 IDE 的几个示例。现在，让我们来看看一些流行的代码编辑器。

Visual Studio Code is a lightweight, open-source code editor by Microsoft that supports a wide range of programming languages and provides features like debugging, syntax highlighting, and version control through extensions.

Visual Studio Code 是 Microsoft 推出的轻量级开源代码编辑器，支持多种编程语言，并通过扩展提供调试、语法突出显示和版本控制等功能。

Another popular editor would be Sublime Text. Sublime Text is a fast, versatile text editor known for its sleek interface, powerful features, and support for a wide range of programming languages through customizable syntax highlighting and plugins.

另一个流行的编辑器是 Sublime Text。Sublime Text 是一款快速、多功能的文本编辑器，以其时尚的界面、强大的功能以及通过可自定义的语法突出显示和插件对多种编程语言的支持而闻名。

And another one is Notepad++. This is a free, open-source, text and source code editor for Windows that offers syntax highlighting, code folding, and a range of plugins to enhance productivity and customization.

另一个是 Notepad++。这是一个适用于 Windows 的免费开源文本和源代码编辑器，提供语法突出显示、代码折叠和一系列插件以提高生产力和自定义。

You may have noticed how the code editors focus primarily on the text contents of the file, where the IDEs expose various tools to manage your code.

您可能已经注意到代码编辑器如何主要关注文件的文本内容，其中 IDE 公开了各种工具来管理您的代码。

These examples are all local programs you can run on your computer, but there are also cloud-based editors that you can use.

这些示例都是可以在计算机上运行的本地程序，但也可以使用基于云的编辑器。

A cloud-based editor is an online tool that allows users to write, edit, and manage code or text directly through a web browser without needing to install software locally.

基于云的编辑器是一种在线工具，允许用户直接通过网络浏览器编写、编辑和管理代码或文本，而无需在本地安装软件。

Let's take a look at a few cloud-based editors.

让我们来看看一些基于云的编辑器。

Replit is an online platform that provides a collaborative environment for coding, allowing users to write, run, and share code in various programming languages directly from a web browser.

Replit 是一个在线平台，提供编码协作环境，允许用户直接从 Web 浏览器编写、运行和共享各种编程语言的代码。

Another popular cloud-based editor is GitHub Codespaces. This is a cloud-based development environment that provides instant access to a fully-configured code editor and development tools directly from GitHub, enabling seamless coding and collaboration.

另一个流行的基于云的编辑器是 GitHub Codespaces。这是一个基于云的开发环境，可直接从 GitHub 即时访问完全配置的代码编辑器和开发工具，从而实现无缝编码和协作。

And another one is Gitpod. Gitpod is a cloud-based development environment that integrates with GitHub and GitLab, offering instant, customizable workspaces for coding, building, and debugging directly from your browser.

另一个是 Gitpod。Gitpod 是一个基于云的开发环境，与 GitHub 和 GitLab 集成，提供即时、可自定义的工作区，用于直接从浏览器进行编码、构建和调试。

And there are many more options. Some options, such as Visual Studio Code, are highly extensible and can work with multiple different project types and languages. Other options might be specifically tailored to a small subset of languages or project types.

还有更多选项。某些选项（例如 Visual Studio Code）具有高度可扩展性，可以使用多种不同的项目类型和语言。其他选项可能是专门针对一小部分语言或项目类型量身定制的。

The application you use might be different for specific projects. You should explore the options to see what will work best for your needs.

对于特定项目，您使用的应用程序可能有所不同。您应该探索这些选项，看看什么最适合您的需求。

## How to Install Visual Studio Code onto Your Computer

To install VS Code, you'll want to visit their website to get the appropriate installer for your operating system. Make sure you visit the VS Code website, and not the Visual Studio website.
要安装 VS Code，您需要访问他们的网站以获取适合您的作系统的安装程序。请确保访问 VS Code 网站，而不是 Visual Studio 网站。

For Windows, you can download an EXE installer. Once you've downloaded it, run the file and the setup wizard will take you through the installation process.
对于 Windows，您可以下载 EXE 安装程序。下载后，运行该文件，安装向导将引导您完成安装过程。

For Mac, you can download a zip archive which contains a .app that you can run. You can also install VS Code via homebrew.
对于 Mac，您可以下载包含可以运行的 .app 的 zip 存档。您还可以通过自制程序安装 VS Code。

Open up the Terminal app on your Mac and run the following command:
在 Mac 上打开终端应用程序并运行以下命令：

brew install --cask visual-studio-code
On Linux, you can download a .deb or .rpm file directly. Once you have it installed, you can use the appropriate executable, or CLI command (typically code), to launch the application. And now you're ready to code.
在 Linux 上，您可以直接下载 .deb 或 .rpm 文件。安装后，您可以使用适当的可执行文件或 CLI 命令（通常是代码 ）来启动应用程序。现在你已经准备好编码了。

## How to Create a Project and Run Your Code Locally in VS Code
如何在 VS Code 中创建项目并在本地运行代码
To get started, you should know that VS Code considers projects to be "workspaces". The workspace is whichever directory you opened in VS Code.
若要开始，您应该知道 VS Code 将项目视为“工作区”。工作区是在 VS Code 中打开的任何目录。

To begin, you will need to use a command line interface to create a new directory for your new project. A directory is another name for the folder.
首先，您需要使用命令行界面为新项目创建一个新目录。目录是文件夹的另一个名称。

Command-line interfaces, or CLI for short, allow you to interact with your operating system through text-based commands. You will learn more about these tools in future lectures.
命令行界面（简称 CLI）允许您通过基于文本的命令与作系统交互。您将在以后的讲座中了解有关这些工具的更多信息。

If you are on Windows, you can use the Command Prompt or PowerShell. If you are on a Mac, you can open up your Terminal app.
如果您使用的是 Windows，则可以使用命令提示符或 PowerShell。如果您使用的是 Mac，则可以打开终端应用程序。

Once the command line is open, navigate to the home directory by typing in the cd ~ command and hitting enter on your keyboard. Then type in the mkdir my-project command and hit enter. mkdir, or "make directory" is the command used to create a new directory. You should then open your new directory with VS Code.
打开命令行后，通过键入 cd ~ 命令并按键盘上的 Enter 键导航到主目录。然后输入 mkdir my-project 命令并按 Enter 键。mkdir，或“make directory”是用于创建新目录的命令。然后，您应该使用 VS Code 打开新目录。

There are also some other graphical ways to create a new directory.
还有一些其他图形方法可以创建新目录。

Depending on your operating system, you might have a context menu (or right-click option) to open VS Code directly from your file explorer. You could also choose to double-click on the VS Code application. If you feel comfortable with the command line you can run the command code /path/to/folder.
根据您的作系统，您可能有一个上下文菜单（或右键单击选项）来直接从文件资源管理器打开 VS Code。您还可以选择双击 VS Code 应用程序。如果您对命令行感到满意，可以运行命令代码 /path/to/folder。

Once it's open, you should see a new blank workspace.
打开后，您应该会看到一个新的空白工作区。

To create a new file, click on the File menu at the top-left corner and select New File.... Then name your file index.html and click on Save.
要创建新文件，请单击左上角的“ 文件 ”菜单，然后选择“ 新建文件...”。然后将您的文件命名为 index.html 并单击保存 。

Now you should see your new file in the explorer tab. Try adding some HTML to your index.html file.
现在您应该在资源管理器选项卡中看到您的新文件。尝试向 index.html 文件添加一些 HTML。

Now you might be tempted to open the HTML file in your browser directly. While that can work, it can also lead to all sorts of unexpected bugs, such as CSS not loading properly.
现在您可能想直接在浏览器中打开 HTML 文件。虽然这可以工作，但它也可能导致各种意外错误，例如 CSS 无法正确加载。

Instead, you should put your HTML file behind a proper web server. That can sound like an intimidating task if you are new to coding, but there's actually a way to do this right from VS Code.
相反，您应该将 HTML 文件放在适当的 Web 服务器后面。如果您是编码新手，这听起来像是一项令人生畏的任务，但实际上有一种方法可以直接从 VS Code 中完成此作。

You'll need to grab the Live Server extension first, which is available for free in the marketplace.
您需要先获取 Live Server 扩展，该扩展可在市场上免费获得。

Click on the extensions tab in the left hand corner and type in Live Server in the search bar.
单击左上角的扩展选项卡，然后在搜索栏中输入 Live Server。

Once you have this installed, you should see a Go live button in your status bar. Make sure you have your HTML file open, and then click it.
安装后，您应该会在状态栏中看到一个上线按钮。确保已打开 HTML 文件，然后单击它。

Your new page should open automatically in a new tab in the browser. If it doesn't then you can go directly to http://localhost:5500/
您的新页面应该会在浏览器的新选项卡中自动打开。如果没有，那么您可以直接转到 http://localhost:5500/

Congratulations! You've now set up your very own project in VS Code, and can view your changes with live server.
祝贺！现在，你已经在 VS Code 中设置了自己的项目，并且可以使用实时服务器查看更改。

## What Are Several Useful Keyboard Shortcuts for Maximizing Productivity in VS Code?
在 VS Code 中最大限度地提高工作效率的几个有用的键盘快捷键有哪些？
You're likely already familiar with some of the basic shortcuts, which are inherited from your operating system. Shortcuts like Ctrl + S to save, Ctrl + C to copy, and Ctrl + V to paste all work in VS Code.
您可能已经熟悉一些从您的作系统继承而来的基本快捷方式。Ctrl + S 保存、Ctrl + C 复制和 Ctrl + V 粘贴等快捷键在 VS Code 中都有效。

But there's a few that are application specific and can still level up your productivity. It's worth noting that some of these shortcuts may differ by operating system.
但有一些是特定于应用程序的，仍然可以提高您的工作效率。值得注意的是，其中一些快捷方式可能因作系统而异。

For example, Shift + Alt + F will run your configured formatter (such as prettier, for a JavaScript project) on the currently opened file.
例如，Shift + Alt + F 将在当前打开的文件上运行您配置的格式化程序（例如 prettier，对于 JavaScript 项目）。

Or Ctrl + Shift + F (Windows), or Cmd + Shift + F (Mac), to search the text contents of all the files in your workspace. Then Ctrl + Shift + H (Windows), or Cmd + Shift + H (Mac), if you want to run a find-and-replace.
或 Ctrl + Shift + F （Windows） 或 Cmd + Shift + F （Mac），以搜索工作区中所有文件的文本内容。然后 Ctrl + Shift + H （Windows） 或 Cmd + Shift + H （Mac），如果要运行查找和替换。

If you need to remove a line, Ctrl + Shift + K (Windows), or Cmd + Shift + K (Mac), will delete it.
如果您需要删除一行，Ctrl + Shift + K （Windows） 或 Cmd + Shift + K （Mac） 将删除它。

Need some extra room for all your code? Ctrl + B (Windows), or Cmd + B (Mac), will hide the sidebar - which has the file list and extensions menu.
需要一些额外的空间来存储您的所有代码？Ctrl + B （Windows） 或 Cmd + B （Mac） 将隐藏侧边栏 - 其中包含文件列表和扩展名菜单。

Or maybe you just can't see your code? Ctrl + plus (Windows), or Cmd + plus (Mac), will increase the scaling of the editor, and Ctrl + minus (Windows), or Cmd + minus (Mac), will decrease it.
或者，也许您只是看不到您的代码？Ctrl + 加号  （Windows） 或 Cmd + 加号  （Mac） 将增加编辑器的缩放比例，Ctrl + 减号  （Windows） 或 Cmd + 减号  （Mac） 将减小缩放比例。

Finally, if you forget any of these shortcuts, you always have Ctrl + Shift + P (Windows), or Cmd + Shift + P (Mac), which opens the command palette for you to select whatever you may need.
最后，如果您忘记了这些快捷键中的任何一个，您始终可以使用 Ctrl + Shift + P （Windows） 或 Cmd + Shift + P （Mac），它会打开命令面板供您选择可能需要的任何内容。

With this knowledge, and maybe a little practice, you are well on your way to becoming a VS Code power user.
有了这些知识，也许还有一点练习，您就可以顺利成为 VS Code 高级用户。

## What Are Some Good VS Code Extensions You Can Use in Your Editor?
您可以在编辑器中使用哪些好的 VS Code 扩展？
Better Comments is an extension that offers special highlighting for specific code comments. For example, it will call out "TODO" comments, as well as syntax to indicate questions or warnings.
Better Comments 是一个扩展，可为特定代码注释提供特殊突出显示。例如，它将调用“TODO”注释，以及指示问题或警告的语法。

Code Spell Checker offers indication when you have spelled something incorrectly in your code. Because it is designed for code files, it will account for things like camel case.
Code Spell Checker 会在代码中拼写错误时提供指示。因为它是为代码文件设计的，所以它会考虑驼峰式命名法之类的内容。

Error Lens will help you catch any highlighted errors in your code. Rather than having to rely on the underline that VS Code shows by default, this extension highlights the entire line and displays the error message.
Error Lens 将帮助你捕获代码中任何突出显示的错误。此扩展程序不必依赖 VS Code 默认显示的下划线，而是突出显示整行并显示错误消息。

Indent Rainbow adds color to your different levels of indentation. In combination with VS Code's native bracket pair colorization, this can dramatically help identify what scope your code is in.
缩进彩虹为不同级别的缩进添加颜色。结合 VS Code 的本机括号对着色，这可以极大地帮助识别代码所处的范围。

Or maybe you're looking for something a bit more practical? Consider an AI assistant, like GitHub Copilot or Tabnine, to offer you inline suggestions as you are writing your code.
或者，也许您正在寻找更实用的东西？考虑使用 AI 助手，例如 GitHub Copilot 或 Tabnine，在您编写代码时为您提供内联建议。

An icon pack, such as VS Code Great Icons, can help make your file tree cleaner and easier to parse at a glance. And an extension like Colorize can help you understand the values in your CSS properties.
图标包（如 VS Code Great Icons）可以帮助使文件树更干净，更易于一目了然地解析。像 Colorize 这样的扩展可以帮助您了解 CSS 属性中的值。

You'll also want language-specific extensions for your projects. If you are using JavaScript, you will likely want ESLint and Prettier to lint and format your code. If you are using TypeScript, you might want Pretty Typescript Errors for easier to read messages.
您还需要为您的项目提供特定于语言的扩展。如果您使用的是 JavaScript，您可能希望 ESLint 和 Prettier 来填充和格式化您的代码。如果您使用的是 TypeScript，您可能需要 Pretty Typescript Errors 以便于阅读消息。

Finally, you can also have a bit of fun with your editor. VS Code Pets offers configurable virtual pets to keep you company while you squash some bugs.
最后，您还可以与编辑器一起享受一些乐趣。VS Code Pets 提供可配置的虚拟宠物，让您在消除一些错误的同时陪伴您。

Power Mode will create flashy effects when you achieve a high enough "combo" by writing more code.
当您通过编写更多代码获得足够高的“组合”时， 电源模式将产生华丽的效果。

Discord Presence will let you show off what you're working on to all of your friends.
Discord Presence 可让您向所有朋友展示您正在做的事情。

And there are so many more extensions out there. Feel free to explore the extension marketplace and see what works best for you.
还有更多的扩展。请随意探索扩展市场，看看什么最适合您。

