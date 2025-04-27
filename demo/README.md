# 几何图形可视化演示程序

这是一个使用matplotlib库创建的几何图形可视化演示程序，用于展示各种几何形状的属性和计算结果。

## 功能特点

- 可视化展示圆形、椭圆、矩形和正方形
- 交互式调整形状参数（如半径、边长等）
- 实时计算并显示面积、周长等几何属性
- 直观比较不同形状的特性
- 支持中文显示

## 运行要求

- Python 3.6+
- matplotlib
- numpy

## 安装依赖

```bash
pip install matplotlib numpy
```

## 中文字体支持

程序默认尝试使用以下中文字体：
- SimHei (黑体)
- Microsoft YaHei (微软雅黑)
- SimSun (宋体)
- Arial Unicode MS
- DejaVu Sans

如果您的系统上没有这些字体，可能会导致中文显示为方块或乱码。您可以：

1. 安装上述任一字体
2. 修改代码中的字体设置，使用您系统上已有的中文字体

## 运行方法

```bash
python geometry_visual_demo.py
```

## 使用说明

1. **切换形状**：
   - 点击顶部的按钮可以切换不同的几何形状（圆形、椭圆、矩形、正方形）

2. **调整参数**：
   - 使用滑块可以调整形状的参数
   - 对于圆形和正方形，只有一个参数（半径/边长）
   - 对于椭圆和矩形，有两个参数（长轴/短轴或宽度/高度）

3. **查看信息**：
   - 右侧会显示当前形状的参数和计算结果（面积、周长等）

## 程序结构

- `GeometryVisualDemo`类：管理整个演示程序
- 形状显示方法：`show_circle()`, `show_ellipse()`, `show_rectangle()`, `show_square()`
- 辅助方法：`clear_shape()`, `update_shape()`, `create_control_panel()`

## 注意事项

- 程序依赖于`geometry`模块，确保该模块在正确的路径下
- 如果遇到导入错误，请检查Python路径设置
- 如果中文显示有问题，请参考"中文字体支持"部分 