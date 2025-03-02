"""
Analysis utilities for the Clinical Trial Analysis Platform.
"""

import streamlit as st
import streamlit.components.v1 as components
from .translations import get_translation

MAP_HTML = """
<!DOCTYPE html>
<html>
  <head>
    <title>Clinical Trial Locations</title>
    <style>
      html, body {
        height: 100%;
        margin: 0;
      }
      gmp-map {
        width: 100%;
        height: 400px;
        border-radius: 10px;
        margin-left: 0%;
      }
      #status {
        position: absolute;
        top: 10px;
        left: 50%;
        transform: translateX(-50%);
        background: white;
        padding: 5px 10px;
        border-radius: 4px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.3);
        display: none;
      }
    </style>
  </head>
  <body>
    <div id="status">Locating you...</div>
    <gmp-map></gmp-map>
    <script>
      (g=>{var h,a,k,p="The Google Maps JavaScript API",c="google",l="importLibrary",q="__ib__",m=document,b=window;b=b[c]||(b[c]={});var d=b.maps||(b.maps={}),r=new Set,e=new URLSearchParams,u=()=>h||(h=new Promise(async(f,n)=>{await (a=m.createElement("script"));e.set("libraries",[...r]+"");for(k in g)e.set(k.replace(/[A-Z]/g,t=>"_"+t[0].toLowerCase()),g[k]);e.set("callback",c+".maps."+q);a.src=`https://maps.${c}apis.com/maps/api/js?`+e;d[q]=f;a.onerror=()=>h=n(Error(p+" could not load."));a.nonce=m.querySelector("script[nonce]")?.nonce||"";m.head.append(a)}));d[l]?console.warn(p+" only loads once. Ignoring:",g):d[l]=(f,...n)=>r.add(f)&&u().then(()=>d[l](f,...n))})({
        key: "AIzaSyAtQhtw4zDJlVQfifApLnplM6urk7juBeQ",
        v: "beta"
      });

      let map;
      let marker;
      const statusDiv = document.getElementById('status');

      async function initMap() {
        try {
          const { Map } = await google.maps.importLibrary("maps");
          const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");
          
          map = document.querySelector('gmp-map').innerMap;
          statusDiv.style.display = 'block';
          
          // Get user's location
          if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
              (position) => {
                const pos = {
                  lat: position.coords.latitude,
                  lng: position.coords.longitude
                };

                // Update map
                map.setCenter(pos);
                map.setZoom(13);

                // Create marker
                if (marker) {
                  marker.setMap(null);
                }
                
                marker = new google.maps.Marker({
                  position: pos,
                  map: map,
                  title: 'Your Location',
                  animation: google.maps.Animation.DROP,
                  icon: {
                    path: google.maps.SymbolPath.CIRCLE,
                    scale: 10,
                    fillColor: '#4285F4',
                    fillOpacity: 1,
                    strokeColor: '#FFFFFF',
                    strokeWeight: 2
                  }
                });

                // Add info window
                const infoWindow = new google.maps.InfoWindow({
                  content: '<div style="padding: 8px;"><strong>Your Location</strong></div>'
                });

                marker.addListener('click', () => {
                  infoWindow.open(map, marker);
                });

                statusDiv.style.display = 'none';
              },
              (error) => {
                statusDiv.textContent = `Error: ${error.message}`;
                console.error('Geolocation error:', error);
                setTimeout(() => {
                  statusDiv.style.display = 'none';
                }, 3000);
              },
              {
                enableHighAccuracy: true,
                timeout: 10000,
                maximumAge: 0
              }
            );
          } else {
            statusDiv.textContent = 'Geolocation is not supported by your browser';
            setTimeout(() => {
              statusDiv.style.display = 'none';
            }, 3000);
          }
        } catch (error) {
          console.error('Error initializing map:', error);
          statusDiv.textContent = 'Error loading map';
          setTimeout(() => {
            statusDiv.style.display = 'none';
          }, 3000);
        }
      }

      initMap();
    </script>
  </body>
</html>
"""

def render_analysis_page(language: str):
    """
    Render the analysis page.
    
    Args:
        language (str): Current language code
    """
    st.title(get_translation('results_title', language))
    
    # Create two columns for the main layout
    col1, col2 = st.columns([2, 3])  # 40% for controls, 60% for map
    
    with col1:
        # Analysis Controls
        st.subheader(get_translation('analysis_controls', language))
        
        analysis_type = st.selectbox(
            (get_translation('select_analysis_type', language)),
            [(get_translation('basic_match', language)), 
             (get_translation('comprehensive_match', language)), 
             (get_translation('advanced_match', language))]
        )
        
        location_range = st.slider(
            (get_translation('maximum_distance', language)),
            0, 500, 100
        )
        
        include_pending = st.checkbox((get_translation('include_pending_trials', language)))
        include_remote = st.checkbox((get_translation('include_remote_trials', language)))
        
        if st.button(get_translation('analysis_start', language)):
            perform_analysis(analysis_type, location_range, include_pending, include_remote)
    
    with col2:
        # Map is always visible
        st.subheader("Clinical Trial Locations")
        components.html(MAP_HTML, height=450)
        st.caption("Map showing nearby clinical trial locations")

def perform_analysis(analysis_type: str, location_range: int, include_pending: bool, include_remote: bool):
    """
    Perform the clinical trial matching analysis.
    """
    # Create a new container for analysis results below the main layout
    st.write("---")  # Add a separator
    st.write("Analyzing data...")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(get_translation('active_diagnoses', st.session_state.language))
        # TODO: Display active diagnoses from patient data
        
        st.subheader(get_translation('past_conditions', st.session_state.language))
        # TODO: Display past conditions from patient data
    
    with col2:
        st.subheader(get_translation('matching_trials', st.session_state.language))
        # TODO: Display matching clinical trials
    
    # Detailed Results
    st.subheader("Detailed Match Analysis")
    # TODO: Display detailed analysis results
    
    # Export Options
    st.download_button(
        "Export Results (PDF)",
        "TODO: Generate PDF report",
        "trial_matches.pdf",
        "application/pdf"
    ) 