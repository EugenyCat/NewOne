"""
Given a variable that stores information on the costs and income of advertising campaigns from different sources.
It is necessary to supplement the original structure with the indicator ROI,
which we calculate by the formula: (revenue / cost - 1) * 100
"""

def caclulate_roi(ad_data:dict) -> dict:
    """Calculate figure ROI (revenue / cost - 1) * 100"""
    result_ad_with_roi = dict(ad_data)
    for adw in result_ad_with_roi.keys():
        roi = round((result_ad_with_roi.get(adw)['revenue']/result_ad_with_roi.get(adw)['cost'] - 1) * 100, 2)
        result_ad_with_roi.get(adw)['ROI'] = roi
    return result_ad_with_roi

results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}

print(caclulate_roi(results))