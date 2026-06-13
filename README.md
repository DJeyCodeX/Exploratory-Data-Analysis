	# Exploratory Data Analysis on Used Cars Data

	## Project Overview

	This project is an exploratory data analysis of a used cars dataset. The main idea was to understand what kind of information is available in the data and how different car features relate to price.

	I treated this as a first step before building any machine learning model. Instead of jumping directly into prediction, I focused on cleaning the data, creating useful features, checking distributions, and looking for patterns that could explain why some cars are priced higher than others.

	## Dataset

	The dataset used in this project is `used_cars_data.csv`. It contains information about used cars such as:

	- Car name
	- Location
	- Year of manufacture
	- Kilometers driven
	- Fuel type
	- Transmission type
	- Owner type
	- Mileage
	- Engine capacity
	- Power
	- Number of seats
	- New car price
	- Used car selling price

	The target column I focused on during the analysis was `Price`, because most of the exploration was about understanding what affects the selling price of a used car.

	### 1. Initial data checks

	Started by loading the data and checking the basic structure using:

	- `head()`
	- `info()`
	- `isnull().sum()`
	- `nunique()`
	- `describe()`

	This helped me understand the number of columns, data types, missing values, and the general shape of the dataset.

	### 2. Cleaning columns with units

	Some columns had numeric values mixed with text units. For example:

	- `Mileage` had values like kmpl or km/kg
	- `Engine` had values in CC
	- `Power` had values in bhp
	- `New_Price` had values with units

	I separated the unit part and converted the numeric part into a cleaner format. This made the columns easier to analyze and use in charts.

	### 3. Dropping unnecessary columns

	The `S.No.` column was removed because it was only a serial number and did not add useful information for analysis.

	### 4. Creating new features

	I created a few new columns to make the data more meaningful:

	| New feature | Why it was created |
	| --- | --- |
	| `Car_Age` | To understand how old the car is instead of only looking at manufacturing year |
	| `Brand` | To compare prices across different car brands |
	| `Model` | To separate the model name from the full car name |
	| `Mileage_unit` | To keep track of the mileage measurement unit |
	| `Engine_unit` | To keep track of the engine measurement unit |
	| `Power_unit` | To keep track of the power measurement unit |
	| `New_Price_Unit` | To keep track of the new price unit |

	Creating `Brand` and `Model` was especially useful because the original `Name` column had both combined together.

	### 5. Standardizing brand names

	Some brand names appeared in slightly different formats. For example:

	- `ISUZU` was changed to `Isuzu`
	- `Mini` was changed to `Mini Cooper`
	- `Land` was changed to `Land Rover`

	This small cleanup helped make brand-level analysis more consistent.

	## Exploratory Data Analysis

	### Univariate analysis

	For numerical columns, I checked:

	- Distribution using histograms
	- Outliers using boxplots
	- Skewness using `.skew()`

	This was useful because columns like `Kilometers_Driven`, `Price`, and `New_Price` can be highly skewed in real-world car data.

	For categorical columns, I used count plots to see the most common values. This helped answer questions like:

	- Which brands appear most often?
	- Which fuel types are common?
	- Are most cars manual or automatic?
	- Which owner type is most frequent?
	- Which locations have more listed cars?

	### Transformation

	I used log transformation on:

	- `Kilometers_Driven`
	- `Price`

	These columns were skewed, so log transformation helped make their distributions easier to compare and analyze.

	This also gave me a better understanding of why transformation is useful before applying certain machine learning models later.

	### Bivariate analysis

	I compared different features against price using pair plots and grouped bar charts.

	Some of the comparisons included:

	- Location vs price
	- Transmission vs price
	- Fuel type vs price
	- Owner type vs price
	- Brand vs price
	- Model vs price
	- Seats vs price
	- Car age vs price

	This part helped me see how price changes across different categories. For example, transmission type, brand, model, and car age are all practical features that can influence resale price.

	### Multivariate analysis

	I used a heatmap to check correlations between numerical variables such as:

	- `Year`
	- `Kilometers_Driven`
	- `Mileage`
	- `Engine`
	- `Seats`
	- `Price`
	- `Car_Age`
	- `New_Price`

	The heatmap helped me understand which numerical columns move together and which ones may have a stronger relationship with price.

	## Concepts Covered

	This project helped me practice the main steps of exploratory data analysis:

	- Reading and understanding a dataset
	- Checking missing values
	- Cleaning columns with mixed text and numbers
	- Creating new features from existing columns
	- Separating categorical and numerical variables
	- Using histograms and boxplots
	- Checking skewness and outliers
	- Applying log transformation
	- Comparing categorical features with price
	- Using pair plots and heatmaps for deeper analysis

	## What I Learned

	The biggest learning from this project was that EDA is not just about making charts. It is about asking better questions from the data.

	For example, instead of only looking at the `Year` column, creating `Car_Age` made the analysis more natural. Similarly, splitting the full car name into `Brand` and `Model` made it easier to compare cars at a more useful level.

	I also learned that real-world datasets are rarely clean. Many columns contain numbers mixed with units, inconsistent names, missing values, or skewed distributions. Cleaning these details properly makes the analysis much more reliable.

	Another important takeaway was that visualizations help reveal patterns that are not obvious from raw tables. Boxplots, count plots, bar charts, pair plots, and heatmaps each gave a different view of the same data.

	## Final Thoughts

	This project gave me hands-on practice with the early stages of a data science workflow. Before any model is built, it is important to understand the data, clean it properly, and explore the relationships between variables.

	The project helped me see how car age, brand, model, fuel type, transmission, usage, and engine-related features can all play a role in used car pricing. It also gave me a stronger foundation for moving from EDA into feature engineering and predictive modeling.
