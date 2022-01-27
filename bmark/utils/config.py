def load_config():
    """Loads dictionary with path names and any other variables set through config.toml

    Returns:
        config: dict
    """
    import toml
    from pathlib import Path
    package_dir = Path(__file__).parent.parent.parent.absolute()
    config_file = package_dir / "config.toml"
    config = {'package_dir': package_dir, 'config_file': config_file}
    toml_config = toml.load(config_file)

    for reference in toml_config:
        config[reference] = {}
        for key in toml_config[reference]:
            if not Path(toml_config[reference][key]).exists():
                print(f'{toml_config[reference][key]} does not exist. Check config.toml')
            config[reference][key] = Path(toml_config[reference][key])

    return config
