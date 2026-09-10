import 'package:flutter/material.dart';

void main() => runApp(const CaseStudyApp());

class CaseStudyApp extends StatelessWidget {
  const CaseStudyApp({super.key});

  @override
  Widget build(BuildContext context) => MaterialApp(
        title: 'EDSanat Case Study',
        theme: ThemeData.dark(useMaterial3: true),
        home: const Scaffold(
          body: Center(
            child: Text('Synthetic mobile catalogue · Offline-ready foundation'),
          ),
        ),
      );
}
