# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

{% if cookiecutter.open_source_license != "Not open source" %}

**License** {{cookiecutter.open_source_license}}
{% endif %}

## Getting Started


### Prerequisites


### Installing

1- Install `cookiecutter`

```
pip install cookiecutter
```

2- Download and configure this project

```
cookiecutter https://github.com/GabrielMMelo/cookiecutter-django
```

3- Configure your database credentials in .env 

4- Install javascript dependences (I'd rather to use `yarn` instead `npm`)

```
yarn install 
```

5- Run the server

```
yarn run dev
```

## Running the tests

Run `pytest`

### Break down into end to end tests


### And coding style tests


## Deployment


## Built With


## Contributing


## Versioning


## Authors

* **{{ cookiecutter.author_name }}** - *Initial work*

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

