import pandas as pd
import plotly.graph_objs as go
import numpy as np
import json

with open("canada.geojson") as f:
    provinces_map = json.load(f) # provinces_map is a dict

# print([d['properties']['name'] for d in provinces_map['features']]) # list for provinces
# ['Quebec', 'Newfoundland and Labrador', 'British Columbia', 'Nunavut', 'Northwest Territories', 'New Brunswick', 'Nova Scotia', 'Saskatchewan', 'Alberta', 'Prince Edward Island', 'Yukon Territory', 'Manitoba', 'Ontario']

df = pd.read_csv('canada_province_data.csv')
df['confirmed_log'] = df.confirmed.map(np.log)

fig = go.Figure(
    go.Choroplethmapbox(
        # ======= featureidkey =======
        # str 类型，默认为id。函数会使用这个参数和 locations 匹配地图单元（比如省份）的名称，以此决定绘制哪些地图单元的轮廓。
        # 通常的形式为 properties.name，其中的 name 需要你自己根据 geojson 文件去指定。
        # 这个很重要，设置不正确会导致地图轮廓显示不出来，一定要保证和 locations 中的所有名称保持一致。
        featureidkey="properties.name",

        # ======== geojson ===========
        # dict 类型，是用于绘制地图轮廓的数据，一般从相应的 geojson 文件中用 json.load 加载进来。
        geojson=provinces_map,

        # ========== locations =======
        # 可以是以下类型：list，numpy array，数字、字符串或者 datetime 构成的 Pandas series。
        # 指定地图单元名称，决定绘制哪些地图单元的轮廓。同样需要注意和 featureidkey 保持一致。
        locations=df.province,

        # ============ z =============
        # 可以是以下类型：list，numpy array，数字、字符串或者 datetime 构成的 Pandas series。
        # 指定地图单元对应的数值，函数会将此值映射到 colorscale 中的某一颜色，然后将此颜色涂到相应的地图单元内。
        # 通常来说是一个 pandas dataframe 中的某一列，即一个 series。
        # 需要注意此参数中值的顺序需要和 locations 保持一致，一一对应.
        z=df.confirmed_log,

        # ========== zauto ===========
        # bool 类型，默认为 True。是否让颜色自动适应 z，即自动计算 zmin 和 zmax，然后据此来映射 colorscale。
        zauto=True,

        # ======== colorscale ========
        # 通常来说是 str 类型，也可以是 list 类型。
        # 指定所使用的 colorscale，可使用的值参见：https://plotly.com/python/builtin-colorscales/。
        colorscale='Oranges',

        reversescale=False,

        # ====== marker_opacity ======
        # float 类型，颜色透明度。
        marker_opacity=0.8,

        # ===== marker_line_width ====
        # float 类型，地图轮廓宽度。
        marker_line_width=0.8,

        customdata=np.vstack((df.province, df.confirmed, df.recoverd, df.death)).T,
        hovertemplate="<b>%{customdata[0]}</b><br><br>"
        + "Confirmed: %{customdata[1]}<br>"
        + "Recoverd: %{customdata[2]}<br>"
        + "Death: %{customdata[3]}<br>"
        + "<extra></extra>",

        # ========= showscale =========
        # bool 类型。是否显示 colorbar，就是地图旁边的颜色条。
        showscale=True,
    )
)

fig.update_layout(
    # ======= mapbox_style ========
    # str 类型，指定 mapbox 风格。
    # 可用的 mapbox 风格列表可参见：https://plotly.com/python/mapbox-layers/#base-maps-in-layoutmapboxstyle。
    # 需要注意的是当你使用["basic", "streets", "outdoors", "light", "dark", "satellite", "satellite-streets"]风格之一时，你就需要指定 mapbox_token（关于如何获取 token 详细可参见：https://github.com/secsilm/2019-nCoV-dash#%E5%85%B3%E4%BA%8E-mapboxtoken）
    mapbox_style="carto-darkmatter",

    # ======== mapbox_zoom ========
    # int 类型，指定地图的缩放级别。
    mapbox_zoom=2,

    # ======= mapbox_center =======
    # dict 类型，key 为 lat（经度）和 lon（纬度），指定初始时地图的中心点。
    mapbox_center={"lat": 72.19, "lon": -82.56},
)

config = {
    "displaylogo": False,
}
fig.write_html('../vis_html/map_demo.html', config=config, auto_open=False)




# import plotly.express as px

# fig = px.choropleth(locations=["CA", "TX", "NY"], locationmode="USA-states", color=[1,2,3], scope="usa")
# fig.write_html('first_figure.html', auto_open=True)


# import plotly.graph_objects as go
# fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
# fig.write_html('first_figure.html', auto_open=True)
