#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 pavle <pavle.portic@tilda.center>
#
# Distributed under terms of the BSD-3-Clause license.

import base64
import random


def generate_primes(start, n):
	'''
	Generate a list of prime numbers between ``start`` and ``n``
	'''
	correction = (n % 6 > 1)
	n = {0: n, 1: n - 1, 2: n + 4, 3: n + 3, 4: n + 2, 5: n + 1}[n % 6]
	sieve = [True] * (n // 3)
	sieve[0] = False
	for i in range(int(n**0.5) // 3 + 1):
		if sieve[i]:
			k = 3 * i + 1 | 1
			sieve[((k * k) // 3)::2 * k] = [False] * ((n // 6 - (k * k) // 6 - 1) // k + 1)
			sieve[(k * k + 4 * k - 2 * k * (i & 1)) // 3::2 * k] = [False] * ((n // 6 - (k * k + 4 * k - 2 * k * (i & 1)) // 6 - 1) // k + 1)

	primes = [3 * i + 1 | 1 for i in range(1, n // 3 - correction) if sieve[i]]

	for i in range(len(primes)):
		if primes[i] > start:
			return primes[i:]

	return []


def calculate_gcd(a, b):
	'''
	Calculate the greatest common denominator
	'''
	while b > 0:
		q = a // b
		a, b = b, a - q * b

	return a


def calculate_lcm(a, b):
	'''
	Calculate the lowest common multiple
	'''
	if a == 0 or b == 0:
		return 0
	return abs((a * b) // calculate_gcd(a, b))


def inverse(e, modulus):
	'''
	Modular multiplicative inverse
	'''
	r_p = e
	r_n = modulus
	s_p, s_n = 1, 0
	while r_n > 0:
		q = r_p // r_n
		r_p, r_n = r_n, r_p - q * r_n
		s_p, s_n = s_n, s_p - q * s_n

	if r_p != 1:
		raise ValueError('No inverse value can be computed' + str(r_p))

	while s_p < 0:
		s_p += modulus

	return s_p


def make_key_pair(length):
	'''
	Create a public/private key pair.

	The key pair is generated from two random prime numbers. The argument
	``length`` specifies the bit length of the number ``n`` shared between
	the two keys.
	'''
	if length < 4:
		raise ValueError('Cannot generate a key of length less than 4 (got {length})'.format(length = length))

	# Min and max length of n to fit inside ``length`` bits
	n_min = 1 << (length - 1)
	n_max = (1 << length) - 1

	# Min and max length of ``p`` and ``q`` so that their product fits into ``length`` bits
	p_min = 1 << (length // 2 - 1)
	p_max = 1 << (length // 2 + 1)

    a = 5

    primes = []
    primes = generate_primes(n_min, n_max)
    # TODO: generate key pair
    
    


def encrypt(pubkey, chunk):
	# TODO: implement encryption
	pass


def decrypt(privkey, chunk):
	# TODO: implement encryption
	pass


class PublicKey():
	def __init__(self, length=0, n=0, e=0):
		self.length = length
		self.n = n
		self.e = e

	def save(self):
		with open('public.key', 'w') as f:
			f.write('{length},{n},{e}'.format(length = self.length, n = self.n, e = self.e))

	def load(self):
		with open('public.key', 'r') as f:
			len_str, n_str, e_str = f.read().split(',')
			self.length = int(len_str)
			self.n = int(n_str)
			self.e = int(e_str)


class PrivateKey():
	def __init__(self, length=0, n=0, d=0):
		self.length = length
		self.n = n
		self.d = d

	def save(self):
		with open('private.key', 'w') as f:
			f.write('{length},{n},{d}'.format(length = self.length, n = self.n, d = self.d))

	def load(self):
		with open('private.key', 'r') as f:
			len_str, n_str, d_str = f.read().split(',')
			self.length = int(len_str)
			self.n = int(n_str)
			self.d = int(d_str)


def string_to_numbers(in_string, chunk_size):
	'''
	Convert a string into a list of numbers where each number represents ``chunk_size`` characters
	'''
	numbers = []
	for i in range(0, len(in_string), chunk_size):
		s = in_string[i:i + chunk_size]
		n = 0
		for c in s:
			n = (n << 8) + ord(c)

		numbers.append(n)

	return numbers


def numbers_to_string(numbers, chunk_size):
	'''
	Convert a list of numbers, where each number represents ``chunk_size`` characters into a string
	'''
	s = ''
	for n in numbers:
		temp_s = ''
		for _ in range(chunk_size):
			temp_s += chr(n & 255)
			n = n >> 8

		s += temp_s[::-1]

	return s


def genkey(length):
	public, private = make_key_pair(length)
	public.save()
	private.save()


def loadkey():
	public = PublicKey()
	public.load()
	private = PrivateKey()
	private.load()
	return public, private


def encrypt_message(message):
	public, private = loadkey()
	chunk_size = public.length // 8

	numbers = string_to_numbers(message, chunk_size)
	encrypted_numbers = [encrypt(public, n) for n in numbers]
	encoded_bytes = b''.join([n.to_bytes(chunk_size, 'big') for n in encrypted_numbers])
	return base64.b64encode(encoded_bytes).decode('ascii')


def decrypt_message(message):
	public, private = loadkey()
	chunk_size = public.length // 8

	decoded = base64.b64decode(message)
	encrypted_numbers = [int.from_bytes(decoded[i:i + chunk_size], 'big') for i in range(0, len(decoded), chunk_size)]
	numbers = [decrypt(private, n) for n in encrypted_numbers]
	return numbers_to_string(numbers, chunk_size)


def main():
	command = input('command> ')
	if command == 'genkey':
		key_length = input('key length> ')
		genkey(int(key_length))
	elif command in ('encrypt', 'decrypt'):
		input_file = input('in file> ')
		output_file = input('out file> ')
		with open(input_file, 'r') as f:
			message = f.read()

		if command == 'encrypt':
			message = encrypt_message(message)
		elif command == 'decrypt':
			message = decrypt_message(message)

		with open(output_file, 'w') as f:
			f.write(message)
	else:
		print('Unexpected command "', command, '"', sep='')


if __name__ == '__main__':
	main()

