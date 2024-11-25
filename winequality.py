from queue import Full


{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "21bfd667-dbf5-4b0f-ae34-d0678763cc3f",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'xgboost'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[5], line 10\u001b[0m\n\u001b[0;32m      8\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01msklearn\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m metrics\n\u001b[0;32m      9\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01msklearn\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01msvm\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m SVC\n\u001b[1;32m---> 10\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mxgboost\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m XGBClassifier\n\u001b[0;32m     11\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01msklearn\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mlinear_model\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m LogisticRegression\n\u001b[0;32m     13\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mwarnings\u001b[39;00m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'xgboost'"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sb\n",
    "\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import MinMaxScaler\n",
    "from sklearn import metrics\n",
    "from sklearn.svm import SVC\n",
    "from xgboost import XGBClassifier\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')\n",
    "df = pd.read_csv('winequality.csv')\n",
    "print(df.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": Full,
   "id": "5e15b035-827b-4388-b9ac-2137bb776e5d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
