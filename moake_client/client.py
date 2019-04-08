import requests
from urllib.parse import quote
import moake_client.config as config
import moake_client.options as options

class Client:
    def __init__(self, opts={}):
        # config
        self.host = config.MOAKE_HOST
        self.port = config.MOAKE_PORT
        # options
        valid_options = options.valid_options
        options_dict = {}
        for option_name in valid_options:
            option_value = opts.get(option_name)
            if option_value is None:
                option_value = options.default_options[option_name]
            setattr(self, option_name.replace('-', '_'), option_value)
            options_dict[option_name] = option_value
        # parameterized options
        self.parameterized_options = options.parameterize_options(options_dict)


    def analyze_text(self, text):
        response = requests.get(
            '{moake_host}:{moake_port}/v1?{options}data={encodedText}'
                .format(
                    moake_host=self.host,
                    moake_port=self.port,
                    options=self.parameterized_options,
                    encodedText=quote(text)
                )
        )
        return response.json()
