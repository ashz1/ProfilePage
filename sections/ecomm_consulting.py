def run():
    import streamlit as st
    import base64

    st.title("Consulting Insights: Indian E-Commerce Market")

    st.markdown("""
    The Indian e-commerce market has demonstrated robust growth, innovation, and resilience. Here are the key insights and trends shaping the industry in 2022 and beyond.
    """)

    st.header("📈 Market Growth & Recovery")
    st.markdown("""
    - Online retail GMV projected to reach **$70B in 2022**, growing at 35% YoY.
    - The sector maintains strong momentum, even as offline retail returns to pre-pandemic levels.
    - E-tailing has seen a **34% CAGR since 2017**.
    """)

    st.header("🛒 Shopper Base & Penetration")
    st.markdown("""
    - **210 million unique online shoppers** expected in 2022, with most new growth from Tier 2+ cities.
    - E-tailing remains underpenetrated outside metros, highlighting untapped potential.
    """)

    st.header("🛍️ Category Diversification & Consumer Preferences")
    st.markdown("""
    - Shoppers are buying a wider range of categories online, increasing annual spend per user.
    - Top reasons for shopping online: **product variety, offers/discounts, and fast delivery**.
    - **Delivery time and return experience** are now critical decision factors.
    """)

    st.header("⚠️ Key Challenges")
    st.markdown("""
    - Product quality, delivery time, and returns/refunds remain top pain points.
    - Lower adoption and spending per shopper in smaller cities highlight the need for tailored solutions and trust-building.
    """)

    st.header("🚀 New E-Commerce Models")
    st.markdown("""
    - **Quick commerce, social commerce, and B2B models** are gaining traction, especially in fashion and grocery.
    - **Awareness and trust** are major barriers to adoption for new models.
    - Quick commerce is growing rapidly, driven by speed and convenience.
    """)

    st.header("💡 Unit Economics & Competitive Landscape")
    st.markdown("""
    - New models face profitability challenges due to high supply chain and marketing costs.
    - Integrated and community-driven models leveraging local networks are finding more success.
    """)

    st.header("🔭 Outlook")
    st.markdown("""
    - Usage is expected to grow across all e-commerce models, especially from smaller cities and new business models.
    - Platforms that solve for trust, affordability, and convenience will be best positioned for long-term growth.
    """)

    st.divider()

    st.header("📄 Full Report")

    pdf_path = "eComm India.pdf"
    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()
        st.download_button(
            label="Download Full Report (PDF)",
            data=pdf_bytes,
            file_name="eComm India.pdf",
            mime="application/pdf"
        )
        st.pdf(pdf_bytes)
    )
