class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_dic = {}
        for word in words:
            word_dic[word] = word_dic.get(word, 0) + 1
        
        def dict_match(dic1, dic2):
            if len(dic1) != len(dic2):
                return False
            for k in dic1:
                if k not in dic2 or dic1[k] != dic2[k]:
                    return False
            return True

        w_len = len(words[0])
        sub_len = len(words) * w_len
        results = []
        for offset in range(w_len):
            if offset+sub_len > len(s):
                break
            wind_dic = {}
            for word_s in range(offset, offset+sub_len, w_len):
                word = s[word_s:word_s+w_len]
                wind_dic[word] = wind_dic.get(word, 0) + 1
            
            if dict_match(wind_dic, word_dic):
                results.append(offset)
            
            for start in range(offset+w_len, len(s)-sub_len+1, w_len):
                rm_word = s[start-w_len:start]
                add_word = s[start+sub_len-w_len:start+sub_len]
                wind_dic[rm_word] -= 1
                if wind_dic[rm_word] == 0:
                    del wind_dic[rm_word]
                wind_dic[add_word] = wind_dic.get(add_word, 0) + 1

                if dict_match(wind_dic, word_dic):
                    results.append(start)
        
        return results