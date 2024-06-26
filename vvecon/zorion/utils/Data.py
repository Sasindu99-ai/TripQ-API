from dataclasses import dataclass

__all__ = ['Data', 'Settings', 'Meta', 'Tracking', 'Navigator']


@dataclass
class Settings:
    head: str
    app_name: str
    app_icon: str
    site_name: str
    logo: str = NotImplemented


@dataclass
class Meta:
    description: str
    keywords: list


@dataclass
class Tracking:
    enabled: bool = False
    google: str = NotImplemented
    hotjar: int = NotImplemented
    facebook: int = NotImplemented


@dataclass
class Navigator:
    enabled: bool = True
    navType: int = 1
    activeTab: str = 'home'


class Data:
    settings: Settings = NotImplemented
    meta: Meta = NotImplemented
    tracking: Tracking = NotImplemented

    navigator: Navigator = NotImplemented
