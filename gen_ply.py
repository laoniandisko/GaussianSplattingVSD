import open3d as o3d
import numpy as np
import torch

# 假设你的点云坐标和颜色数据是numpy数组
# points.shape -> (n, 3) 例如: [[x1, y1, z1], [x2, y2, z2], ...]
# colors.shape -> (n, 3) 例如: [[r1, g1, b1], [r2, g2, b2], ...]
coords = torch.load("/mnt/chenjh/lx_projx/GaussianDreamer_VSD/points.pth").view(-1, 3).to('cpu').numpy()
rgb = torch.load("/mnt/chenjh/lx_projx/GaussianDreamer_VSD/sampled_color.pth").view(-1, 3).to('cpu').detach().numpy()

# 创建一个PointCloud对象
pcd = o3d.geometry.PointCloud()

# 设置点云的坐标
pcd.points = o3d.utility.Vector3dVector(coords)

# 设置点云的颜色（确保颜色在0到1之间）
pcd.colors = o3d.utility.Vector3dVector(rgb / 255.0) 
o3d.io.write_point_cloud("/mnt/chenjh/lx_projx/GaussianDreamer_VSD/output.ply", pcd)