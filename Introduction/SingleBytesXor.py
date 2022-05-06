from xor import*
from dataclasses import dataclass, astuple
from typing import Optional
from collections import*
from string import*
from pprint import*
from base64 import*
frequency = {'a': 0.07743208627550165,
 'b': 0.01402241586697527,
 'c': 0.02665670667329359,
 'd': 0.04920785702311875,
 'e': 0.13464518994079883,
 'f': 0.025036247121552113,
 'g': 0.017007472935972733,
 'h': 0.05719839895067157,
 'i': 0.06294794236928244,
 'j': 0.001267546400727001,
 'k': 0.005084890317533608,
 'l': 0.03706176274237046,
 'm': 0.030277007414117114,
 'n': 0.07125316518982316,
 'o': 0.07380002176297765,
 'p': 0.017513315119093483,
 'q': 0.0009499245648139707,
 'r': 0.06107162078305546,
 's': 0.061262782073188304,
 't': 0.08760480785349399,
 'u': 0.030426995503298266,
 'v': 0.01113735085743191,
 'w': 0.02168063124398945,
 'x': 0.0019880774173815607,
 'y': 0.022836421813561863,
 'z': 0.0006293617859758195}
@dataclass(order=True)

class ScoredGuess:
	score: float = float ('inf')
	key: Optional[int] = None
	ciphertext: Optional[bytes] = None
	plaintext:Optional[bytes] = None

	@classmethod
	def from_key(cls, ct, key_val):
		full_key = bytes([key_val]) * len(ct)
		pt = bytes_xor(ct,full_key)
		score = score_text(pt)
		return cls(score, key_val, ct, pt)
def get_frequency(text, letters):
	cnt = Counter()
	for i in letters:
		cnt[i] = text.count(i)
	total = sum(cnt.values())
	return {letter:cnt[letter]/total for letter in letters} 
def score_text(text:bytes) -> float: #Score the Likelihood with English Written Language
	score = 0.0
	l = len(text)
	for letter, freq in frequency.items():
		actual_freq = text.count(ord(letter))/l
		err = abs(freq - actual_freq);
		score += err
	return score
def crack_xor_cipher(ciphertext:bytes) -> tuple: # Find the best answer and key can guess form Ciphertext
	best_guess = ScoredGuess()
	for key in range(256):
		guess_cur = ScoredGuess.from_key(ciphertext,key)
		best_guess = min(best_guess, guess_cur)
		#if(key == 53): print(guess_cur)
	return best_guess
def crack_xor_cipher_statistic(ciphertext:bytes)-> list[bytes]:
	result = []
	for key in range(256):
		full_key = bytes([key])*len(ciphertext)
		plaintext = bytes_xor (ciphertext,full_key)
		guess_cur = (score_text(plaintext),plaintext)
		result.append(guess_cur)
	result.sort()
	return result
if __name__ == "__main__":
	ciphertext = b16decode("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104",casefold=True)
	best_guess = crack_xor_cipher_statistic(ciphertext)
	pprint(best_guess)

	
