import streamlit as st
import geopandas as gpd
import pandas as pd
import folium
from shapely import wkt
from streamlit_folium import folium_static
import plotly.graph_objects as go
import os

def run():
    st.markdown("""
        <style>
            .metric-card {
                background: linear-gradient(135deg, #1f77b4, #aec7e8);
                border-radius: 8px;
                padding: 16px;
                color: white;
                margin-bottom: 16px;
            }
            .section-header {
                font-size: 1.8rem;
                margin-top: 32px;
                margin-bottom: 16px;
                border-bottom: 2px solid #ccc;
                padding-bottom: 8px;
            }
            .insight-box {
                background: #f9f9f9;
                border-left: 4px solid #1f77b4;
                padding: 12px;
                margin-bottom: 16px;
            }
        </style>
    """, unsafe_allow_html=True)

    @st.cache_data
    def load_data():
        neighborhoods = gpd.read_file("Boston_Neighborhoods.shp")
        survey = pd.read_csv("Survey_responses.csv")
        df = pd.read_csv("merg_padl.csv")
        df['geometry'] = df['geometry'].apply(wkt.loads)
        merged = gpd.GeoDataFrame(df, geometry='geometry', crs="EPSG:4326")
        return neighborhoods, survey, merged

    neighborhoods, survey_df, merged_gdf = load_data()

    analysis = st.selectbox(
        "Select Analysis Section",
        [
            "📈 Market Overview",
            "🗺️ Interactive Map",
            "📉 Safety Analysis",
            "🏘️ Neighborhood Stats",
            "📝 Survey Insights",
            "⚖️ Comparative Analysis",
            "📑 View Full Report Slides"  # <-- New option here
        ]
    )

    if analysis == "📈 Market Overview":
        # existing code ...
        avg_2000 = merged_gdf["FY2000.AV_mean"].mean()
        avg_2021 = merged_gdf["FY2021.AV_mean"].mean()
        delta_pct = (avg_2021 - avg_2000) / avg_2000 * 100

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f'<div class="metric-card"><h4>2000 Avg Value</h4><h2>${avg_2000:,.0f}</h2></div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div class="metric-card"><h4>2021 Avg Value</h4><h2>${avg_2021:,.0f}</h2></div>', unsafe_allow_html=True)
        with col3:
            st.markdown(f'<div class="metric-card"><h4>Change</h4><h2>{delta_pct:.1f}%</h2></div>', unsafe_allow_html=True)

        bar_data = {
            "Year": ["2000", "2021"],
            "Average Value": [avg_2000, avg_2021]
        }
        fig = go.Figure(
            data=[go.Bar(x=bar_data["Year"], y=bar_data["Average Value"], marker_color=["#1f77b4", "#ff7f0e"])]
        )
        fig.update_layout(
            title="Citywide Average Property Value: 2000 vs 2021",
            yaxis_title="Avg Value ($)",
            xaxis_title="Year"
        )
        st.plotly_chart(fig, use_container_width=True)

    elif analysis == "🗺️ Interactive Map":
        # existing code for interactive map
        metric = st.selectbox(
            "Select Metric",
            ["TOTAL_VALUE_mean", "LIVING_AREA_mean", "RES_FLOOR_mean", "robbery", "bike_stations_count"]
        )
        m = folium.Map(location=[42.3601, -71.0589], zoom_start=12, tiles="CartoDB positron")
        folium.Choropleth(
            geo_data=merged_gdf,
            data=merged_gdf,
            columns=["neighborhood", metric],
            key_on="feature.properties.neighborhood",
            fill_color="YlOrBr",
            legend_name=metric.replace("_", " "),
            highlight=True,
            nan_fill_color="white"
        ).add_to(m)
        folium_static(m, height=600)

    elif analysis == "📉 Safety Analysis":
        # existing safety analysis code
        crime_types = ["robbery", "drug", "assault", "SHOOTING"]
        total_crime = merged_gdf[crime_types].sum(axis=1)
        df_crime = merged_gdf.assign(total_crime=total_crime).sort_values("total_crime", ascending=False)
        top = st.slider("Show top N neighborhoods by total crime", 5, 20, 10)
        fig = go.Figure(
            data=[go.Bar(
                x=df_crime.head(top)["neighborhood"],
                y=df_crime.head(top)["total_crime"],
                marker_color="#1f77b4"
            )]
        )
        fig.update_layout(
            title="Total Crime Incidents",
            xaxis_title="Neighborhood",
            yaxis_title="Total Crimes"
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('<div class="insight-box">📌 <strong>Insight:</strong> Dorchester and Roxbury have the highest crime counts, indicating priority areas for community policing.</div>', unsafe_allow_html=True)

    elif analysis == "🏘️ Neighborhood Stats":
        # existing neighborhood stats code
        stats = merged_gdf.groupby("neighborhood").agg({
            "LIVING_AREA_mean": "mean",
            "RES_FLOOR_mean": "mean"
        }).reset_index()
        fig1 = go.Figure(
            data=[go.Bar(
                x=stats.sort_values("LIVING_AREA_mean", ascending=False).head(10)["neighborhood"],
                y=stats.sort_values("LIVING_AREA_mean", ascending=False).head(10)["LIVING_AREA_mean"],
                marker_color="#1f77b4"
            )]
        )
        fig1.update_layout(
            title="Top 10 Neighborhoods by Avg Living Area",
            xaxis_title="Neighborhood",
            yaxis_title="Avg Living Area (sq ft)"
        )
        fig2 = go.Figure(
            data=[go.Bar(
                x=stats.sort_values("RES_FLOOR_mean", ascending=False).head(10)["neighborhood"],
                y=stats.sort_values("RES_FLOOR_mean", ascending=False).head(10)["RES_FLOOR_mean"],
                marker_color="#ff7f0e"
            )]
        )
        fig2.update_layout(
            title="Top 10 Neighborhoods by Avg Residential Floors",
            xaxis_title="Neighborhood",
            yaxis_title="Avg Floors"
        )
        col1, col2 = st.columns(2)
        col1.plotly_chart(fig1, use_container_width=True)
        col2.plotly_chart(fig2, use_container_width=True)

    elif analysis == "📝 Survey Insights":
        # existing survey insights code
        st.dataframe(survey_df)
        summary = survey_df.describe().T
        st.table(summary.style.format({
            "mean": "{:.2f}", "std": "{:.2f}", "min": "{:.0f}", "max": "{:.0f}"
        }))

    elif analysis == "⚖️ Comparative Analysis":
        # existing comparative analysis code
        choices = st.multiselect(
            "Select neighborhoods (3–6)",
            merged_gdf["neighborhood"].unique().tolist(),
            ["Back Bay", "Roxbury", "Dorchester"]
        )
        metrics = ["TOTAL_VALUE_mean", "LIVING_AREA_mean", "RES_FLOOR_mean", "bike_stations_count"]
        if 3 <= len(choices) <= 6:
            comp = merged_gdf[merged_gdf["neighborhood"].isin(choices)]
            mean_vals = comp.groupby("neighborhood")[metrics].mean().reset_index()

            norm_means = mean_vals.copy()
            for metric in metrics:
                min_val = mean_vals[metric].min()
                max_val = mean_vals[metric].max()
                if max_val > min_val:
                    norm_means[metric] = (mean_vals[metric] - min_val) / (max_val - min_val)
                else:
                    norm_means[metric] = 0

            fig = go.Figure()
            for _, row in norm_means.iterrows():
                fig.add_trace(go.Scatterpolar(
                    r=row[metrics].values,
                    theta=[m.replace("_", " ") for m in metrics],
                    fill="toself",
                    name=row["neighborhood"]
                ))
            fig.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
                showlegend=True,
                title="Neighborhood Comparison (Normalized)"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Please select between 3 and 6 neighborhoods.")

    elif analysis == "📑 View Full Report Slides":
        st.markdown("## 📊 Full Report Slides")
        slides_folder = "slides"

        if os.path.exists(slides_folder):
            slide_images = sorted(
                [img for img in os.listdir(slides_folder) if img.endswith(".jpeg")],
                key=lambda x: int(''.join(filter(str.isdigit, x))) if any(c.isdigit() for c in x) else 0
            )
            for slide in slide_images:
                slide_path = os.path.join(slides_folder, slide)
                st.image(slide_path, use_column_width=True, caption=slide.replace(".jpeg", "").replace("Slide", "Slide "))
        else:
            st.warning("Slides folder not found. Please check your directory structure.")
