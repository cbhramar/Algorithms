#include <bits/stdc++.h>

using namespace std;

int gcd(int i, int j) {
	if (j == 0) return i;
	else return gcd(j, i % j);
}

int lcm(int i, int j) {
	return (i/gcd(i,j))*j;
}

int max(int i, int j) {
	if (i > j)
		return i;
	return j;
}

void findRepetition(vector<int>& functions, int& initial, int& period) {
	int n = functions.size();
	
	for (unsigned i = 0; i < n; ++i) {
		vector<int> occurs(n, -1);
		int j = 0;
		int k = i;
		
		while(occurs[k] == -1) {
			occurs[k] = j;
			++j;
			k = functions[k];
		}
		
		initial = max(initial, occurs[k]);
		int periodCandidate = j - occurs[k];
		period = lcm(periodCandidate, period);
	}
}

void closestFriendSubset(vector<int>& functions, int& smallestSubset) {
	int n = functions.size();
	vector<int> closestFriendTo(n);
	for (unsigned i = 0; i < n; ++i)
		++closestFriendTo[functions[i]];

	vector<bool> included(n,false);

	bool found = true;

	while (found) {
		found = false;
		for (int i = 0; i < n; i++)
			if ((closestFriendTo[i] == 0) && !included[i] && !included[functions[i]]) {
				included[functions[i]] = true;
				closestFriendTo[functions[functions[i]]]--;
				smallestSubset++;
				found = true;
			}
		if (!found) {
			for (int i = 0; (i < n) && !found; i++)
				if (!included[i] && !included[functions[i]]) {
					included[i] = true;
					closestFriendTo[functions[i]]--;
					smallestSubset++;
					found = true;
				}
		}
	}
}

int main(int argc, char const *argv[]) {
	int functionRange;
	cin >> functionRange;
	vector<int> functions(functionRange);
	for (unsigned i = 0; i < functionRange; ++i) {
		cin >> functions[i];
	}

	int initial = 0, period = 1;
	findRepetition(functions, initial, period);
	cout << initial << " " << period << endl;
	int smallestSubset = 0;
	closestFriendSubset(functions, smallestSubset);
	cout << smallestSubset << endl;

	return 0;
}