import streamlit as st
import pandas as pd
from datetime import datetime

class CancerEducationApp:
    def __init__(self):
        self.podcast_data = {
            "chris_beat_cancer": {
                "name": "Chris Beat Cancer",
                "host": "Chris Wark",
                "episodes": [
                    {
                        "title": "Nutrition and Cancer Recovery",
                        "duration": "1:15:23",
                        "key_points": [
                            "Whole food plant-based diet",
                            "Anti-inflammatory foods",
                            "Success stories"
                        ]
                    }
                ]
            }
        }

def main():
    st.set_page_config(
        page_title="Cancer Education Hub",
        page_icon="🎗️",
        layout="wide"
    )

    st.title("Cancer Education Hub 🎗️")
    st.markdown("---")

if __name__ == "__main__":
    main()
