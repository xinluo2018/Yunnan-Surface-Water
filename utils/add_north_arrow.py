## author: ziyue dou
## creat: 2025.5.16  
# modify: 2025.5.16, xin luo
## des: add north_arrow to the map

from matplotlib.patches import Polygon

def add_north_arrow(ax, loc=(0.95, 0.85), size = [0.05, 0.05],
               color_narrow_left='white', color_narrow_right='black',
               edge_color_narrow='gray', edge_width_narrow=1, 
               N_label = True, font_N=12, color_N = 'black',               
               projection=None, 
               text_offset=0.02):
    """add north arrow to the map"""
    if projection is None:
        projection = ax.projection
    
    xmin, xmax, ymin, ymax = ax.get_extent()
    
    # center of the north_arrow
    x_center = xmin + (xmax - xmin) * loc[0]
    y_center = ymin + (ymax - ymin) * loc[1]
    
  
    width = (xmax - xmin) * size[0]
    height = (ymax - ymin) * size[1] * 2

    # define top of the north_arrow
    top = (x_center, y_center + height / 2)
    bottom_left = (x_center - width / 2, y_center - height / 2)
    bottom_right = (x_center + width / 2, y_center - height / 2)
    mid_bottom = (x_center, y_center - height / 2 * 0.2)

    # add north arrow
    ax.add_patch(Polygon([top, bottom_left, mid_bottom], 
                facecolor=color_narrow_left, edgecolor=edge_color_narrow, 
                linewidth=edge_width_narrow, transform=projection))  # narrow left
    ax.add_patch(Polygon([top, bottom_right, mid_bottom], 
                facecolor=color_narrow_right, edgecolor=edge_color_narrow,
                linewidth=edge_width_narrow, transform=projection))  # narrow left
    
    # add N label
    if N_label:
        ax.text(x_center, y_center + height / 2 + (ymax - ymin) * text_offset, 'N',
            fontsize=font_N, ha='center', va='bottom', color=color_N, transform=projection)

