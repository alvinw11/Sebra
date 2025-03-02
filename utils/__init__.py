"""
Clinical Trial Analysis Platform utilities package.
"""

from .translations import get_translation, SUPPORTED_LANGUAGES
from .auth import render_login_page
from .medical_info import render_medical_info_page
from .analysis import render_analysis_page
__all__ = [
    'get_translation',
    'SUPPORTED_LANGUAGES',
    'render_login_page',
    'render_medical_info_page',
    'render_analysis_page'
] 