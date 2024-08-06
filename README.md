# Design Writeup

## Author: Nicholas Dow

## Overview

For this project, I created the following classes:

- **Dataset**: Represents the entire dataset containing multiple documents.
- **Document**: Represents a single document within a dataset.
- **Chunk**: Represents a segment of a document.
- **Chunker**: Breaks up text into smaller chunks and applies the embedder to that text.
- **Embedder**: Allows you to choose which embedding you would want for your text data.
- **Loader**: A superclass that allows for loading different file formats.
- **Storage**: Allows you to choose the storage format for the Python dataset object on the disk.
- **Pipeline**: An object/class that is constructed from a loader, chunker, embedder, and storage object.

Additionally, I would consider creating an operations class (not yet implemented), which contains a function for the date it was applied, which may be stored in the dataset object in addition to the modified data. This would allow us to keep track of changes we made to the data. 

The loaders use ‘glob’ to flatten the directory hierarchy and store that information as a path since the structure often contains valuable data. This also makes the processing more general.

## Design Rationale

- **Modularity**: Each class has a clear, single responsibility, making the system modular and easier to maintain or extend. For instance, TensorFlow or PyTorch embedders could be added without altering the existing system structure.
- **Polymorphism**: I used polymorphism to allow for interchangeable components within the pipeline. Different loaders can handle various data formats, and different chunkers can split documents based on different criteria. This approach ensures flexibility and ease of extension.
- **Flexibility**: I wanted the design to support flexible data models. Initially, Parquet was considered for storage due to its efficiency, but the lack of flexibility led to choosing a more adaptable format like Dill (similar to Pickle), which simplifies modifications and allows for dynamic data structures. Storing chunks directly in columnar format would be valid but might require a lot of hardcoding that becomes tedious when we update our data model. It might also be difficult to recover the data from this format should we make updates on new versions.
- **Extensibility**: The design anticipates future enhancements, such as adding a change history to datasets or integrating advanced embedders, without significant core architecture changes. Although I couldn't complete the entire ambitious design, the system is structured to accommodate features like dataset operation history, data streaming mode, data versioning, API integration, internet data reading, and more efficient storage options.

## Class Interactions

- **Pipeline** is constructed out of Loader, Chunker, Embedder, and Storage objects to process raw data into our dataset object and store it locally on the disk.
- **Dataset** contains multiple Document objects, which contain multiple Chunk objects.

## Adding More Datasets

To add more datasets, place the raw datasets in the designated input folder. The pipeline will then process these datasets into a standardized format and store them in the output folder when the pipeline is run and constructed in the Python script. If a dataset with the same name already exists and the overwrite flag is set, then the stored data is overwritten. In the future, I would like to enhance the pipeline to track changes and updates to datasets, improving dataset management.

## Using This Code in Application Logic for Data Upload

In an ideal scenario, I would create a server or frontend UI where users can upload data. Right now, this code would run in the backend, constructing the pipeline based on file format and model configuration hints. For example, it would select a chunker that fits the context width of the target language model.

## Testing

During development, I would try to run the code with an example dataset while using the debugger to ensure end-to-end functionality. With specific specifications from the end user, I would create unit tests for the classes and develop the code using those tests. For maintenance, I would implement unit tests to ensure changes do not break existing functionality and would use Jenkins to verify code coverage and pass tests before merging pull requests.

## Example Usage

See `example.py` in the repository for an example of how this pipeline can be run.
