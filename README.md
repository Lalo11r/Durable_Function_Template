# Durable Function Template

This project is a template for Azure Durable Functions using Python. It provides a basic structure to create and deploy Durable Functions locally.



## Setup and Deployment

### Requirements

- Python 3.7 or higher
- Azure Functions Core Tools
- Azure Storage Emulator (Includen in windows sdk)

### Instalación

1. Clone the repository:
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd Durable_Function_Template
    ```

2. Create and activate de virtual environment:
    ```sh
    python -m venv .venv
    .venv\Scripts\activate  # On Windows
    source .venv/bin/activate  # On macOS/Linux
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Main functions
- Http_Start (Client): HTTP entry point that starts the orchestration.
- Orchestrator: Coordinates the execution of activities.
- Activity: Performs a specific task and returns a result.

![Durable Function Components](https://s3.amazonaws.com/ebooks.syncfusion.com/LiveReadOnlineFiles/azure-durable-functions-succinctly/Images/durable-functions-components.png)



### Local Execution

To run the project locally, use the following command:

```sh
func start
```

If you want the console to display detailed execution debugging, use:

```sh
func host start --verbose
```

## Contributions

Contributions are welcome. Please open an issue or pull request to discuss any changes you would like to make.