{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e6b13bd6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "def load_and_clean_data(path):\n",
    "    df = pd.read_csv(path)\n",
    "\n",
    "    df[\"Engine Fuel Type\"] = df[\"Engine Fuel Type\"].fillna(\n",
    "        df[\"Engine Fuel Type\"].mode()[0]\n",
    "    )\n",
    "\n",
    "    df[\"Market Category\"] = df[\"Market Category\"].fillna(\"Unknown\")\n",
    "\n",
    "    df = df.drop(columns=[\"Model\"])\n",
    "\n",
    "    return df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1b8ce843",
   "metadata": {},
   "outputs": [],
   "source": [
    "def split_features_target(df):\n",
    "    X = df.drop(columns=[\"MSRP\"])\n",
    "    y = df[\"MSRP\"]\n",
    "    return X, y\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "27d6b286",
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    df = load_and_clean_data(\"cars.csv\")\n",
    "    X, y = split_features_target(df)\n",
    "\n",
    "    print(df.shape)\n",
    "    print(X.shape, y.shape)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "de12fdbf",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "venv",
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
   "version": "3.12.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
