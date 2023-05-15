##10 几行 Python 代码，轻松实现 PDF 转文字（OCR）

### 介绍

光学字符识别 （OCR） 是一种允许用户将包含文本的扫描文档、图像或 PDF 转换为可搜索和可编辑的数字格式的技术。在本文中，我们将探讨如何设置和使用 Pytesseract（一种使用 Google 的 Tesseract 引擎的 OCR 工具）和 Imagemagick（一个强大的图像处理库）在 Windows 和 Mac 计算机上进行 OCR 扫描的 PDF。

### 设置 Pytesseract 和 Imagemagick

#### Win 电脑

第 1 步：下载并安装 Python 要开始使用，请从官方网站（https://www.python.org/downloads/windows/）下载并安装最新版本的 Python。确保在安装过程中选择“将 Python 添加到 PATH”选项。

第 2 步：安装 Pytesseract 打开命令提示符并运行以下命令以安装 Pytesseract Python 库：

```
pip install pytesseract
```

第 3 步：安装 Tesseract OCR 从官方 GitHub 存储库 （https://github.com/UB-Mannheim/tesseract/wiki） 下载 Tesseract OCR 安装程序。运行安装程序并按照安装说明进行操作。安装完成后，将 Tesseract 添加到您的系统 PATH 中。

第 4 步：安装 Imagemagick 访问 Imagemagick 下载页面 （https://imagemagick.org/script/download.php） 并下载相应的 Windows 二进制版本。运行安装程序并按照安装说明进行操作。确保在安装过程中选择“安装旧版实用程序（例如转换）”选项。

#### Mac 电脑

步骤 1：安装自制软件 Homebrew 是 Mac 的软件包管理器，可简化许多应用程序的安装过程。如果您没有安装 Homebrew，请按照官方网站（https://brew.sh/）上的说明进行操作。

第 2 步：安装 Python 打开终端并运行以下命令通过自制软件安装 Python：

```
pip install pytesseract
```

第 4 步：安装 Tesseract OCR 运行以下命令，通过自制软件安装 Tesseract OCR：

```
brew install tesseract
```

第 5 步：安装 Imagemagick 运行以下命令，通过 Homebrew 安装 Imagemagick：

brew install imagemagick

### 安装中文语言包

以 mac 为例，将 assets/chi_sim.traineddata 文件拷贝到你的 Tesseract 安装目录/opt/homebrew/share/tessdata

### 执行

然后在终端 （Mac） 或命令提示符 （Windows） 中运行以下命令，将“input.pdf”替换为扫描的 PDF 的路径，将“output.txt”替换为所需的输出文件名：

```
python main.py input.pdf output.txt
```
