    public List<Boolean> camelMatch(String[] queries, String pattern) {
        List<Boolean> res = new ArrayList<>();
        for (String query : queries)
            res.add(isMatch(query, pattern));
        return res;
    }

    private boolean isMatch(String query, String pattern) {
        int i = 0;
        for (char c: query.toCharArray()) {
            if (i < pattern.length() && c == pattern.charAt(i))
                i++;
            else if (c < 'a')
                return false;
        }
        return i == pattern.length();
    }