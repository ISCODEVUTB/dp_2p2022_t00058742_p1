import 'ie.dart';

class Human extends Characters {
  List<String>? get Powers => super.Powers = null;

  void attack() => print('Attack...');
  void defense() => print('Defense...');
  void levelup() {
    print('***¡Level UP!***');
  }
}
