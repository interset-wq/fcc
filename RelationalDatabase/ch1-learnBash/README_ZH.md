# Bash

文件夹(folder)，就是目录(directory)，二者没有区别

大多数命令都可以使用 `flag` 来增强命令，具体有哪些flag，可以通过 `<命令名> --help` 查看

## 路径操作

### pwd

```bash
pwd
```

输出当前工作路径

### ls

```bash
ls
```

列出(list) 当前路径下的文件和文件夹（不列出这些文件夹的子目录）

使用flag:

```bash
ls -l
```

列出(list) 当前路径下的文件和文件夹的详细信息（创建时间，大小等信息，仍然不列出子目录）

### cd

切换目录(change directory)

```bash
cd <path>
```

常用：

- `cd ..` 回到上级目录
- `cd ../..` 回到上级目录的上级目录

