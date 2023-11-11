# 解いた問題
## 1. <a href="https://leetcode.com/problems/two-sum/">Two Sum</a>
リスト内の2つの整数を加算してtargetの値になる組み合わせを探索し、
見つかったインデックス番号を返す。<br>
ただし、同じインデックスの整数は使用不可。<br>
解いた言語：python

## 9. <a href="https://leetcode.com/problems/palindrome-number/">Palindrome Number</a>
整数が回文になっているかを確認し、回文ならtrue、違うならfalseを返す。<br>
解いた言語：python

## 13. <a href="https://leetcode.com/problems/roman-to-integer/description/">Roman to Integer</a>
ローマ数字を整数に変換する。ローマ数字は左から右に大きい数字を表す文字が並べられ、各記号を整数に変換し、加算することで変換する。例えば、27はXXVIIと表し、X+X+V+I+Iで算出する。ただし、以下は減算する。<br>
IがV or Xの前につく時、IVは4(5 - 1)、IXは9(10 - 1)。<br>
XがL or Cの前につく時、XLは40(50 - 10)、XCは90(100 - 10)。<br>
CがD or Mの前につく時、CDは400(500 - 100)、CMは900(1000 - 100)。<br>
気付かなかったが、右の文字から処理（大小比較）していけばシンプルに実装できる。変換表は以下。<br>
|Symbol|Value|
|----|----|
|I|1|
|V|5|
|X|10|
|L|50|
|C|100|
|D|500|
|M|1000|

解いた言語：python

## 14. <a href="https://leetcode.com/problems/longest-common-prefix/description/">Longest Common Prefix
</a>
複数の文字列が含まれるリストから最長の共通する接頭文字列を見つける。見つからない場合は、空文字を返す。<br>
気付かなかったが、リストの内で最短の文字列と最長の文字列を比較すればよかった。<br>
解いた言語：python

## 20. <a href="https://leetcode.com/problems/valid-parentheses/description/?source=submission-noac">Valid Parentheses</a>
文字列が有効な文字列か判定する。文字列を構成する文字は、(, ), {, }, [, ]である。<br>
有効かどうか判定する条件は以下<br>
1. 開き括弧は同じ種類の括弧で閉じなければならない
1. 開き括弧は正しい順序で閉じなければならない
1. すべての閉じ括弧には、対応する開き括弧がある
解いた言語：python

## 22. <a href="https://leetcode.com/problems/merge-two-sorted-lists/description/">Merge Two Sorted Lists</a>
2つのソート済みの連結リストを1つの連結リスト（ソート済み）に結合する。<br>
結合した連結リストの先頭ノードを返す。<br>
解いた言語：python
