import 'package:flutter/material.dart';

class NavigationBarApp extends StatelessWidget {
  const NavigationBarApp({super.key});

    @override
  Widget build(BuildContext context) {
    return Scaffold(
      bottomNavigationBar: BottomNavigationBar(
        items: const [
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: 'Home',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.settings),
            label: 'Settings',
          ),
        ],
      ),
      appBar: AppBar(
        title: const Text('Navigation bar'),
      ),
    );
  }
}