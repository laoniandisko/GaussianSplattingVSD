#!/bin/bash

# 设置文件夹路径
folder_path="/mnt/chenjh/lx_projx/GaussianDreamer_VSD/*"

# 设置大小阈值（以KB为单位，4MB = 4096KB）
size_limit=4096

# 遍历文件夹
for folder in $folder_path; do
    # 获取文件夹大小
    folder_size=$(du -sk "$folder" | cut -f1)
    # 比较文件夹大小
    if [ $folder_size -lt $size_limit ]; then
        # 文件夹小于4MB，添加到Git
        git add "$folder"
        echo "Added $folder to Git (size: $folder_size KB)"
    else
        echo "Skipped $folder (size: $folder_size KB)"
    fi
done
