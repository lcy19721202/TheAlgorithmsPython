#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
几何类图形化演示程序
使用matplotlib可视化展示各种几何形状
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Rectangle, Circle, Polygon as MplPolygon
from matplotlib.widgets import Button, Slider, TextBox
import sys
import os
import matplotlib

# 设置中文字体支持
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'SimSun', 'Arial Unicode MS', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 添加父目录到系统路径，以便导入geometry模块
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from geometry.geometry import Angle, Side, Ellipse as GeoEllipse, Circle as GeoCircle, Polygon, Rectangle as GeoRectangle, Square

class GeometryVisualDemo:
    """几何形状可视化演示类"""
    
    def __init__(self):
        """初始化演示程序"""
        self.fig = plt.figure(figsize=(12, 8))
        self.fig.suptitle('几何形状可视化演示', fontsize=16, y=0.98)
        
        # 创建主绘图区域，调整位置留出控件空间
        self.ax = self.fig.add_axes([0.1, 0.2, 0.55, 0.65])
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.grid(True)
        self.ax.set_aspect('equal')
        
        # 初始化形状
        self.current_shape = None
        self.shape_patch = None
        
        # 创建控制面板
        self.create_control_panel()
        
        # 默认显示圆形
        self.show_circle()
    
    def create_control_panel(self):
        """创建控制面板"""
        # 创建形状选择按钮 - 在顶部水平排列
        button_width = 0.15
        button_height = 0.05
        button_y = 0.9
        spacing = 0.02
        
        button_ax1 = plt.axes([0.1, button_y, button_width, button_height])
        button_ax2 = plt.axes([0.1 + (button_width + spacing), button_y, button_width, button_height])
        button_ax3 = plt.axes([0.1 + 2 * (button_width + spacing), button_y, button_width, button_height])
        button_ax4 = plt.axes([0.1 + 3 * (button_width + spacing), button_y, button_width, button_height])
        
        self.button_circle = Button(button_ax1, '圆形')
        self.button_ellipse = Button(button_ax2, '椭圆')
        self.button_rectangle = Button(button_ax3, '矩形')
        self.button_square = Button(button_ax4, '正方形')
        
        self.button_circle.on_clicked(lambda event: self.show_circle())
        self.button_ellipse.on_clicked(lambda event: self.show_ellipse())
        self.button_rectangle.on_clicked(lambda event: self.show_rectangle())
        self.button_square.on_clicked(lambda event: self.show_square())
        
        # 创建参数滑块 - 在左侧垂直排列
        slider_x = 0.1
        slider_width = 0.4
        slider_height = 0.02
        
        self.param1_ax = plt.axes([slider_x, 0.12, slider_width, slider_height])
        self.param2_ax = plt.axes([slider_x, 0.07, slider_width, slider_height])
        
        self.param1_slider = Slider(self.param1_ax, '半径', 1, 10, valinit=3.31)
        self.param2_slider = Slider(self.param2_ax, '高度', 1, 10, valinit=5.11)
        
        self.param1_slider.on_changed(self.update_shape)
        self.param2_slider.on_changed(self.update_shape)
        
        # 创建信息显示区域 - 在右侧
        self.info_ax = plt.axes([0.72, 0.3, 0.25, 0.3])
        self.info_ax.axis('off')
        self.info_text = self.info_ax.text(0, 0.5, '', fontsize=12, va='center')
    
    def clear_shape(self):
        """清除当前形状"""
        if self.shape_patch:
            self.shape_patch.remove()
            self.shape_patch = None
        self.ax.clear()
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.grid(True)
        self.ax.set_aspect('equal')
    
    def update_shape(self, val=None):
        """更新形状"""
        if self.current_shape == 'circle':
            self.show_circle()
        elif self.current_shape == 'ellipse':
            self.show_ellipse()
        elif self.current_shape == 'rectangle':
            self.show_rectangle()
        elif self.current_shape == 'square':
            self.show_square()
    
    def show_circle(self):
        """显示圆形"""
        self.clear_shape()
        self.current_shape = 'circle'
        
        # 更新滑块标签
        self.param1_slider.label.set_text('半径')
        self.param2_ax.set_visible(False)
        self.param2_slider.visible = False
        
        # 获取参数
        radius = self.param1_slider.val
        
        # 创建几何对象
        geo_circle = GeoCircle(radius)
        
        # 创建matplotlib图形
        circle = Circle((0, 0), radius, fill=False, color='blue')
        self.ax.add_patch(circle)
        self.shape_patch = circle
        
        # 更新信息
        info = f'圆形\n半径: {radius:.2f}\n面积: {geo_circle.area:.2f}\n周长: {geo_circle.perimeter:.2f}'
        self.info_text.set_text(info)
        
        plt.draw()
    
    def show_ellipse(self):
        """显示椭圆"""
        self.clear_shape()
        self.current_shape = 'ellipse'
        
        # 更新滑块标签
        self.param1_slider.label.set_text('长轴')
        self.param2_slider.label.set_text('短轴')
        self.param2_ax.set_visible(True)
        self.param2_slider.visible = True
        
        # 获取参数
        major_radius = self.param1_slider.val
        minor_radius = self.param2_slider.val
        
        # 创建几何对象
        geo_ellipse = GeoEllipse(major_radius, minor_radius)
        
        # 创建matplotlib图形
        ellipse = Ellipse((0, 0), major_radius*2, minor_radius*2, fill=False, color='green')
        self.ax.add_patch(ellipse)
        self.shape_patch = ellipse
        
        # 更新信息
        info = f'椭圆\n长轴: {major_radius:.2f}\n短轴: {minor_radius:.2f}\n面积: {geo_ellipse.area:.2f}\n周长: {geo_ellipse.perimeter:.2f}'
        self.info_text.set_text(info)
        
        plt.draw()
    
    def show_rectangle(self):
        """显示矩形"""
        self.clear_shape()
        self.current_shape = 'rectangle'
        
        # 更新滑块标签
        self.param1_slider.label.set_text('宽度')
        self.param2_slider.label.set_text('高度')
        self.param2_ax.set_visible(True)
        self.param2_slider.visible = True
        
        # 获取参数
        width = self.param1_slider.val
        height = self.param2_slider.val
        
        # 创建几何对象
        geo_rectangle = GeoRectangle(width, height)
        
        # 创建matplotlib图形
        rect = Rectangle((-width/2, -height/2), width, height, fill=False, color='red')
        self.ax.add_patch(rect)
        self.shape_patch = rect
        
        # 更新信息
        info = f'矩形\n宽度: {width:.2f}\n高度: {height:.2f}\n面积: {geo_rectangle.area():.2f}\n周长: {geo_rectangle.perimeter():.2f}'
        self.info_text.set_text(info)
        
        plt.draw()
    
    def show_square(self):
        """显示正方形"""
        self.clear_shape()
        self.current_shape = 'square'
        
        # 更新滑块标签
        self.param1_slider.label.set_text('边长')
        self.param2_ax.set_visible(False)
        self.param2_slider.visible = False
        
        # 获取参数
        side_length = self.param1_slider.val
        
        # 创建几何对象
        geo_square = Square(side_length)
        
        # 创建matplotlib图形
        square = Rectangle((-side_length/2, -side_length/2), side_length, side_length, fill=False, color='purple')
        self.ax.add_patch(square)
        self.shape_patch = square
        
        # 更新信息
        info = f'正方形\n边长: {side_length:.2f}\n面积: {geo_square.area():.2f}\n周长: {geo_square.perimeter():.2f}'
        self.info_text.set_text(info)
        
        plt.draw()
    
    def run(self):
        """运行演示程序"""
        plt.show()

def main():
    """主函数"""
    demo = GeometryVisualDemo()
    demo.run()

if __name__ == "__main__":
    main() 