# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest

import sys
sys.path.append("..")

from p1 import solve_p1, halfway_around_match


S_FINAL = "95148459654114155731698478149499917967976774762713244751317162642456177966287315776144295221229668557345231" \
          "126344516323349319921138783846159463566669942298294778262331733368397843812326132686395971977717922859931932" \
          "113894846656274376158483618451298413163535411626489918195274822452395397648581629522794579255572612191334495" \
          "945445882948547117441577527886532414273333978987892959627599834177887388958581991645747477325224917936659995" \
          "145418265722557627783466922298236688468856575469127374595946864895749851132621593435396398147159398461755451" \
          "451962378532688837474214731899342321483475178595695839513348665638845455276972256252441571591386994632555139" \
          "663859339872993852642499434826793515355585155228722331338358366991294136434469472547825829749896951763288118" \
          "739414159347981853619459797651925421593225765377745522747761795783327346321659364239421527531473491471972661" \
          "892317791834266435195425266725323385881436535172293871662154422659895625775321224885925835136317478274233696" \
          "142532538156157599235241551416878281617386114885947828533952915163142953681928649872181232386177163857434441" \
          "687947625592992915791298415174261326875477968539612595459531813493336662659449824995638877172377724277265467" \
          "844881584455537289257474773567236829982654825474435937766729476455933465952323314658756826111625315518939418" \
          "869683169128471126487291434896188825338697199443135247471737687874594876917124324262121991237873175554438724" \
          "944399738239971473835185775232936799766516695646754445981758291547851448654145393217559841355425967211736486" \
          "311259251598892274716484266836192513555124892344996832838588987751215695272519869174695143144349749645576151" \
          "648657347618532174852364428349418111939987432468392239354768285193143593127626776677279826156311795464857642" \
          "174138482349418789527258257566968527998698835779613879432612585277299544635572321116152316188622256285354648" \
          "841156347399863384795324678755714618769694783133572288891817296125649897186894623729952347484198352739148996" \
          "235719643392725179876436249396589499559268329665187478738424732664388677496682865739371762659157832117483222" \
          "243412881787176534727815279942556563352115264368622141112946342549642538551671968288415745277214158574316664" \
          "7191938727971366274357874252166721759"


class CountNextSameTests(unittest.TestCase):
    """Tests for P1"""

    def test_first_string(self):
        actual = solve_p1("1122")
        expected = 3
        self.assertEqual(actual, expected)

    def test_second_string(self):
        actual = solve_p1("1111")
        expected = 4
        self.assertEqual(actual, expected)

    def test_third_string(self):
        actual = solve_p1("1234")
        expected = 0
        self.assertEqual(actual, expected)


    def test_final_part1(self):
        actual = solve_p1(S_FINAL)
        print("part1 results: {}".format(actual))

    def test_part2_seq1(self):
        actual = halfway_around_match("1212")
        expected = 6
        self.assertEqual(actual,expected)

    def test_part2_seq2(self):
        actual = halfway_around_match("1221")
        expected = 0
        self.assertEqual(actual,expected)

    def test_part2_seq3(self):
        actual = halfway_around_match("123425")
        expected = 4
        self.assertEqual(actual,expected)

    def test_part2_seq4(self):
        actual = halfway_around_match("123123")
        expected = 12
        self.assertEqual(actual,expected)

    def test_part2_seq5(self):
        actual = halfway_around_match("12131415")
        expected = 4
        self.assertEqual(actual,expected)

    def test_part2_final(self):
        actual = halfway_around_match(S_FINAL)
        print("part2 results: {}".format(actual))

if __name__ == "__main__":
    unittest.main()
