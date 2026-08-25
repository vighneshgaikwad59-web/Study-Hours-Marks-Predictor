# Study Hours → Marks Predictor

A simple linear regression model that predicts a student's marks based on
the number of hours they studied. Built with `scikit-learn` as a beginner
project to practice supervised learning with `LinearRegression`.

## How it works

The model is trained on a small sample dataset:

| Hours Studied | Marks Obtained |
|----------------|-----------------|
| 1              | 20              |
| 2              | 30              |
| 3              | 40              |
| 6              | 50              |

`LinearRegression` fits a straight line through this data, learning the
relationship between hours studied (input feature) and marks obtained
(target). Once trained, it can predict marks for any number of study
hours entered by the user.

## Usage

```bash
pip install -r requirements.txt
python study_hours_predictor.py
```

You'll be prompted to enter the number of hours studied, and the script
will print the predicted marks.

**Example:**

```
Enter how many hours you have studied: 5
If you study 5.0 hours, you are predicted to score 46.43 marks
```

## Requirements

- Python 3.x
- scikit-learn

## Notes

This is a toy example with only 4 data points, meant for learning the
basic `fit()` / `predict()` workflow of scikit-learn — not for real
predictive accuracy. A larger, more diverse dataset would be needed for
a meaningful model.
