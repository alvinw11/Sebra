// Language Selector Functionality
document.addEventListener('DOMContentLoaded', function() {
    // Handle language selection
    const languageSelect = document.querySelector('[data-testid="stSelectbox"]');
    if (languageSelect) {
        languageSelect.addEventListener('change', function(e) {
            // Trigger page reload to apply new language
            window.location.reload();
        });
    }
});

// Form Validation
function validateForm(formElement) {
    const inputs = formElement.querySelectorAll('input[required]');
    let isValid = true;
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            isValid = false;
            highlightError(input);
        } else {
            removeError(input);
        }
    });
    
    return isValid;
}

function highlightError(element) {
    element.style.borderColor = 'rgba(56, 144, 199, 0.7)';
    element.style.boxShadow = '0 0 10px rgba(28, 40, 114, 0.3)';
}

function removeError(element) {
    element.style.borderColor = 'rgba(255, 255, 255, 0.5)';
    element.style.boxShadow = '0 0 10px rgba(30, 60, 114, 0.2)';
}

// Dynamic Form Handling
function setupDynamicFormFields() {
    // Handle smoking status dependent fields
    const smokingStatus = document.querySelector('#smoking-status');
    const smokingFields = document.querySelector('#smoking-details');
    
    if (smokingStatus && smokingFields) {
        smokingStatus.addEventListener('change', function(e) {
            smokingFields.style.display = 
                ['Current Smoker', 'Former Smoker'].includes(e.target.value) 
                    ? 'block' 
                    : 'none';
        });
    }
    
    // Handle alcohol use dependent fields
    const alcoholUse = document.querySelector('#alcohol-use');
    const alcoholFields = document.querySelector('#alcohol-details');
    
    if (alcoholUse && alcoholFields) {
        alcoholUse.addEventListener('change', function(e) {
            alcoholFields.style.display = 
                ['Occasional', 'Moderate', 'Heavy'].includes(e.target.value)
                    ? 'block'
                    : 'none';
        });
    }
}

// File Upload Handling
function handleFileUpload(fileInput) {
    fileInput.addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (file) {
            // Show loading indicator
            const loadingIndicator = document.createElement('div');
            loadingIndicator.className = 'loading-indicator';
            loadingIndicator.textContent = 'Uploading...';
            fileInput.parentNode.appendChild(loadingIndicator);
            
            // Simulate file upload (replace with actual upload logic)
            setTimeout(() => {
                loadingIndicator.remove();
                showUploadSuccess();
            }, 2000);
        }
    });
}

function showUploadSuccess() {
    const successMessage = document.createElement('div');
    successMessage.className = 'upload-success';
    successMessage.textContent = 'File uploaded successfully!';
    document.body.appendChild(successMessage);
    
    setTimeout(() => {
        successMessage.remove();
    }, 3000);
}

// Tab Navigation Enhancement
function enhanceTabNavigation() {
    const tabs = document.querySelectorAll('.stTab');
    if (tabs.length) {
        tabs.forEach(tab => {
            tab.addEventListener('click', function() {
                // Add smooth transition
                document.querySelectorAll('.stTab-content').forEach(content => {
                    content.style.transition = 'opacity 0.3s ease';
                });
            });
        });
    }
}

// Initialize all functionality
function initializeApp() {
    setupDynamicFormFields();
    
    const fileInputs = document.querySelectorAll('input[type="file"]');
    fileInputs.forEach(handleFileUpload);
    
    enhanceTabNavigation();
    
    // Add form validation to all forms
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!validateForm(form)) {
                e.preventDefault();
            }
        });
    });
}

// Call initialization when DOM is loaded
document.addEventListener('DOMContentLoaded', initializeApp);

// Add smooth scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Add responsive design handlers
window.addEventListener('resize', function() {
    const width = window.innerWidth;
    const elements = document.querySelectorAll('.responsive-element');
    
    elements.forEach(element => {
        if (width < 768) {
            element.classList.add('mobile');
        } else {
            element.classList.remove('mobile');
        }
    });
}); 

/**Google Maps API
 * @license
 * Copyright 2024 Google LLC. All Rights Reserved.
 * SPDX-License-Identifier: Apache-2.0
 */
let map;
let infoWindow;
let userMarker;


function initMap() {
    // Default location (if geolocation fails)
    const defaultLocation = { lat: 37.7749, lng: -122.4194 }; // San Francisco

async function init() {
  const {InfoWindow} = await google.maps.importLibrary("maps");

  map = document.querySelector('gmp-map').innerMap;
  infoWindow = new InfoWindow({pixelOffset: {height: -37}});

  // Get the earthquake data (JSONP format).
  // This feed is a copy from the USGS feed, you can find the originals here:
  //   http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
  const script = document.createElement("script");
  script.src = "https://storage.googleapis.com/mapsdevsite/json/quakes.geo.json";
  document.head.appendChild(script);
}

function showQuakeInfo(position, feature) {
  const content = `
    <div style="padding: 8px">
      <h2 style="margin-top: 0">${feature.getProperty('place')}</h2>
      <h3>Magnitude ${feature.getProperty('mag')}</h3>
      <p>${new Date(feature.getProperty('time'))}</p>
      <a href="${feature.getProperty('url')}" target="new">View on USGS</a>
    </div>
  `;

  infoWindow.setOptions({content, position});
  infoWindow.open({map, shouldFocus: false});
}

// Defines the callback function referenced in the jsonp file.
window.eqfeed_callback = (data) => {
  map.data.addGeoJson(data);
  map.data.setStyle((feature) => ({
    title: feature.getProperty('place')
  }));
  map.data.addListener('click', (e) => showQuakeInfo(e.latLng, e.feature));
}
   // Try to get user's current location
   if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
        (position) => {
            const userLocation = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };

            // Set map center to user's location
            map.setCenter(userLocation);

            // Add a marker for the user's location
            userMarker = new google.maps.Marker({
                position: userLocation,
                map: map,
                title: "You are here!",
                icon: {
                    url: "https://maps.google.com/mapfiles/ms/icons/blue-dot.png", // Custom marker icon
                }
            });
        },
        () => {
            alert("Geolocation failed. Please allow location access.");
        }
    );
} else {
    alert("Geolocation is not supported by your browser.");
}
}
init();