# Cloth Recyclability GUI Application

This is a simple graphical user interface (GUI) application that allows users to input textiles and their corresponding percentages, and determine the recyclability of each textile based on predefined lists of recyclable and non-recyclable textiles.

## Motivation

The Cloth Recyclability GUI Application is designed to help individuals determine the recyclability of different textiles commonly used in clothing. Recycling textiles is an important step towards promoting sustainability and reducing waste in the fashion industry. This application aims to provide users with a convenient way to assess the recyclability of their clothing items based on predefined lists of recyclable and non-recyclable textiles.


## Prerequisites

- Python 3.x
- Tkinter library (usually included in Python installations)


## Getting Started

1. Clone the repository or download the source code files.
2. Ensure you have Python and Tkinter installed on your system.
3. Run the script `cloth_recyclability_gui.py` using Python.
4. The GUI window will open.
5. Enter textiles and their percentages, one per line, in the provided text entry box.
6. Click the "Process" button to determine the recyclability of the textiles.
7. The recyclability results will be displayed in the text box below.

## Usage 

- Enter textiles and percentages:
- In the text entry box, enter each textile followed by a colon (:) and the percentage.
- Each textile should be on a separate line.
- Example:
 ```
 cotton: 50
 polyester: 30
 silk: 20
 ```
- Click the "Process" button to determine the recyclability of the textiles.
- The results will be displayed in the text box below:
- If the mixed textiles contain more than 50% non-recyclable textile, the message "Pick another outfit: More than 50% of non-recyclable textiles" will be shown.
- If the mixed textiles contain more than 50% recyclable textile, the message "This outfit can be partly recycled: More than 50% of recyclable textiles" will be shown.
- For each individual textile, it will show whether it can be recycled, cannot be recycled, or if it cannot be determined

## Functionality
The Cloth Recyclability GUI Application offers the following functionality:

1. Inputting Textiles: Users can input textiles and their corresponding percentages using the provided text entry box. Each textile should be entered on a separate line in the format "textile: percentage." The application accepts both recyclable and non-recyclable textiles.

2. Recyclability Determination: Based on the user input, the application determines the recyclability of each textile. It checks whether each textile belongs to the predefined list of recyclable or non-recyclable textiles and calculates the overall recyclability percentage of the mixed textiles.

3. Recyclability Results: The application displays the recyclability results in the text box below the input area. It provides information on whether the mixed textiles can be fully recycled, cannot be recycled, or are partly recyclable based on the percentage of recyclable and non-recyclable textiles in the mix.


## Scenarios 
The Cloth Recyclability GUI Application can be utilized in various scenarios, including:

1. Personal Wardrobe Assessment: Users can input the textiles from their wardrobe and determine the recyclability of their clothing items. This can help individuals make more informed decisions about their fashion choices and promote sustainability in their personal lives.

2. Sustainable Fashion Brands: Fashion brands and designers can use this application to assess the recyclability of their clothing collections. It can aid in the selection of more environmentally friendly materials and guide the design process towards more sustainable practices.

3. Educational Tool: The application can be used as an educational tool to raise awareness about textile recycling and sustainability. It can be incorporated into workshops, classrooms, or online platforms to engage users in understanding the environmental impact of different textiles.

4. Recycling Centers and Organizations: Recycling centers and organizations focused on textile recycling can utilize this application to assess the recyclability of textile donations. It can assist in the sorting process and guide decisions on recycling or repurposing textile materials.


## Lessons Learned

1. One of the challenges faced in building this project is lacking knowledge on what product could be recycled or not. 
2. Designing an intuitive and visually appealing user interface can be challenging, especially if you're new to GUI development. It requires careful consideration of layout, color schemes, and user interaction to ensure a pleasant user experience
