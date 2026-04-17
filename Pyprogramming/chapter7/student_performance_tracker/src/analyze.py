# Modules
import matplotlib.pyplot as plt

class Analyzer:
    def __init__(self, X, root_path = "images/"):
        """
        Class instantiation

        Parameters:
        X(dict): Dictionary dataset
        root_path(str): Location to save the image file root path

        Return:
        
        image(png): Analysis matplotlib figure
        """
        self.X = X
        self.root_path = root_path

    def analyze_age_results(self, filename):
        """
        A linear plot of age Vs. the G3 results

        Parameters:
        filename(str): The name of the file(image)

        Return:
        dict(file saving results)
        """
        # Axis values
        x = [row["age"] for row in self.X]
        y = [row["G3"] for row in self.X]

        # Plotting the line plot
        plt.scatter(x, y)
        plt.title("Age Vs. G3 Performance")
        plt.xlabel("Age")
        plt.ylabel("Results(G3)")
        

        # Saving the plot
        filepath = f"{self.root_path}{filename}"
        
        # Save the figure
        plt.savefig(filepath)

        return {"Saved": True, "path": filepath}