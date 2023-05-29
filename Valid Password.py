{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a3f3fa6f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "\n",
    "def new_password(password):\n",
    "    try:\n",
    "        if len(password) < 6:\n",
    "            print(\"Password is too short! minimum length of transaction password: 6\")\n",
    "            return False\n",
    "        if len(password) > 12:\n",
    "            print(\"Password is too long! maximum length of transaction password is 12\")\n",
    "            return False    \n",
    "        \n",
    "        lowercase = re.search(\"[a-z]\", password)\n",
    "        uppercase = re.search(\"[A-Z]\", password)\n",
    "        digit = re.search(\"[0-9]\", password)\n",
    "        symbol = re.search(\"[$#@]\", password)\n",
    "        \n",
    "        if not lowercase:\n",
    "            print(\"Password must contain at least 1 lowercase letter\")\n",
    "        \n",
    "        if not uppercase:\n",
    "            print(\"Password must contain at least 1 uppercase letter\")\n",
    "        \n",
    "        if not digit:\n",
    "            print(\"Password must contain at least 1 digit\")\n",
    "        \n",
    "        if not symbol:\n",
    "            print(\"Password must contain at least 1 character from [$#@]\")\n",
    "        \n",
    "        if not (lowercase and uppercase and digit and symbol):\n",
    "            return False\n",
    "        \n",
    "        return True\n",
    "    \n",
    "    except TypeError:\n",
    "        return False\n",
    "\n",
    "print(\"Kindly enter a new password for your account\")\n",
    "print(\"P.S. Your password must contain the following:\")\n",
    "print(\"1. At least 1 letter between [a-z]\")\n",
    "print(\"2. At least 1 number between [0-9]\")\n",
    "print(\"3. At least 1 letter between [A-Z]\")\n",
    "print(\"4. At least 1 character from [$#@]\")\n",
    "print(\"5. Minimum length of transaction password: 6\")\n",
    "print(\"6. Maximum length of transaction password: 12\")\n",
    "\n",
    "# Test the password validity\n",
    "password = input(\"Enter the password: \")\n",
    "if new_password(password):\n",
    "    print(\"Password is valid.\")\n",
    "else:\n",
    "    print(f\"The password '{password}' is invalid.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f79b27e0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dc7bbb9b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fc782a23",
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
