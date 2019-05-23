chrome_options = webdriver.ChromeOptions()
download_dir = os.path.join(BASEDIR, 'usFile')
# ----------页面打印版pdf下载-----------------
appState = {
    "recentDestinations": [
        {
            "id": "Save as PDF",
            "origin": "local"
        }
    ],
    "selectedDestinationId": "Save as PDF",
    "version": 2
}
# ----------网页版pdf直接下载-----------------
profile = {
    "plugins.plugins_list": [{
        "enabled": False, "name": "Chrome PDF Viewer"
    }],  # Disable Chrome's PDF Viewer
    "download.default_directory": download_dir,
    "download.extensions_to_open": "applications/pdf",
    'printing.print_preview_sticky_settings.appState': json.dumps(appState),
    'savefile.default_directory': download_dir
}
chrome_options.add_experimental_option("prefs", profile)