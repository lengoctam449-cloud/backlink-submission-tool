class BacklinkSubmissionTool:
    def __init__(self):
        self.features = {
            "auto_submit_backlinks": True,
            "scalable": True,
            "safe_automation": True,
            "proxy_support": True,
            "customizable_settings": True,
            "multi_platform_support": True,
            "real_time_monitoring": True,
            "easy_integration": True,
            "user_friendly_interface": True,
            "reporting": True
        }

    def submit_backlinks(self, backlinks, target_sites):
        if self.features["auto_submit_backlinks"]:
            # Implement the logic for automated backlink submission
            pass
    
    def monitor_submissions(self):
        if self.features["real_time_monitoring"]:
            # Implement real-time monitoring logic
            pass
    
    def generate_reports(self):
        if self.features["reporting"]:
            # Implement reporting logic to track submitted backlinks
            pass
    
    def use_proxies(self, proxies):
        if self.features["proxy_support"]:
            # Implement proxy logic to prevent IP bans
            pass

    def customize_submission(self, settings):
        if self.features["customizable_settings"]:
            # Implement logic to customize submission settings
            pass

    def integrate_with_other_tools(self):
        if self.features["easy_integration"]:
            # Implement logic to integrate with other SEO tools
            pass

    def display_features(self):
        for feature, is_enabled in self.features.items():
            status = "Enabled" if is_enabled else "Disabled"
            print(f"{feature.replace('_', ' ').title()}: {status}")

# Example usage
tool = BacklinkSubmissionTool()
tool.display_features()
