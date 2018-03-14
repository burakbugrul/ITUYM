#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int N, M;

long long int res;

string text, pattern, current;

void z_function(string s, int start){
	
	int n = (int) s.length();
	vector<int> z(n);
	
	for (int i = 1, l = 0, r = 0; i < n; ++i) {
		if (i <= r)
			z[i] = min (r - i + 1, z[i - l]);
		while (i + z[i] < n && s[z[i]] == s[i + z[i]])
			++z[i];
		if (i + z[i] - 1 > r)
			l = i, r = i + z[i] - 1;
	}
	
	for( int i=start ; i<(int)z.size() ; i++ )
		res += z[i];
}

int main(){
	
	std::ios::sync_with_stdio(false);
	
	cin >> N >> M >> text >> pattern;
	
	reverse(pattern.begin(), pattern.end());
	
	for( int i=0 ; i<(int)pattern.size() ; i++ ){
		current += pattern[i];
		reverse(current.begin(), current.end());
		z_function(current + "." + text, i+1);
		reverse(current.begin(), current.end());
	}
	
	cout << res << endl;
	return 0;
}
