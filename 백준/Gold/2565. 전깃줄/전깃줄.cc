#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n;
int dp[101], cnt[101];
vector<pair<int, int>> li;

int main() {
	cin >> n;
	
	for (int i = 0; i < n; i++) {
		int s, e;
		cin >> s >> e;
		li.push_back({ s, e });
	}

	sort(li.begin(), li.end());
	int ans = 0;

	for (int i = 0; i < n; i++) {
		cnt[i] = 1;
		for (int j = 0; j < i; j++) {
			if (li[j].second < li[i].second) {
				cnt[i] = max(cnt[i], cnt[j]+1);
			}
		}
	}
	
	for (int i = 0; i < n; i++) {
		ans = max(ans, cnt[i]);
	}
	cout << n-ans;
}