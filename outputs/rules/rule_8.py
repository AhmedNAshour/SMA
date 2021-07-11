def findDecision(obj): #obj[0]: Fever, obj[1]: Tiredness, obj[2]: Dry-Cough, obj[3]: Difficulty-in-Breathing, obj[4]: Sore-Throat, obj[5]: Pains, obj[6]: Nasal-Congestion, obj[7]: Runny-Nose, obj[8]: Diarrhea, obj[9]: Smell and taste loss
   # {"feature": "Smell and taste loss", "instances": 26739, "metric_value": 0.9509, "depth": 1}
   if obj[9]>0:
      # {"feature": "Nasal-Congestion", "instances": 21982, "metric_value": 0.7855, "depth": 2}
      if obj[6]<=0.0:
         # {"feature": "Difficulty-in-Breathing", "instances": 12815, "metric_value": 0.9721, "depth": 3}
         if obj[3]<=0:
            # {"feature": "Pains", "instances": 8747, "metric_value": 0.9908, "depth": 4}
            if obj[5]<=0:
               # {"feature": "Sore-Throat", "instances": 4584, "metric_value": 0.9139, "depth": 5}
               if obj[4]<=0:
                  # {"feature": "Runny-Nose", "instances": 2970, "metric_value": 0.4384, "depth": 6}
                  if obj[7]<=0:
                     # {"feature": "Dry-Cough", "instances": 1634, "metric_value": 0.6453, "depth": 7}
                     if obj[2]<=0:
                        # {"feature": "Tiredness", "instances": 1055, "metric_value": 0.8191, "depth": 8}
                        if obj[1]>0:
                           # {"feature": "Diarrhea", "instances": 590, "metric_value": 0.9238, "depth": 9}
                           if obj[8]>0:
                              # {"feature": "Fever", "instances": 399, "metric_value": 1.0, "depth": 10}
                              if obj[0]>0:
                                 return 'no'
                              elif obj[0]<=0:
                                 return 'yes'
                              else:
                                 return 'yes'
                           elif obj[8]<=0:
                              return 'yes'
                           else:
                              return 'yes'
                        elif obj[1]<=0:
                           # {"feature": "Diarrhea", "instances": 465, "metric_value": 0.6058, "depth": 9}
                           if obj[8]<=0:
                              # {"feature": "Fever", "instances": 265, "metric_value": 0.8273, "depth": 10}
                              if obj[0]<=0:
                                 return 'yes'
                              elif obj[0]>0:
                                 return 'yes'
                              else:
                                 return 'yes'
                           elif obj[8]>0:
                              return 'yes'
                           else:
                              return 'yes'
                        else:
                           return 'yes'
                     elif obj[2]>0:
                        return 'yes'
                     else:
                        return 'yes'
                  elif obj[7]>0:
                     return 'yes'
                  else:
                     return 'yes'
               elif obj[4]>0:
                  # {"feature": "Fever", "instances": 1614, "metric_value": 0.7821, "depth": 6}
                  if obj[0]>0:
                     return 'no'
                  elif obj[0]<=0:
                     return 'yes'
                  else:
                     return 'yes'
               else:
                  return 'no'
            elif obj[5]>0:
               # {"feature": "Runny-Nose", "instances": 4163, "metric_value": 0.7075, "depth": 5}
               if obj[7]<=0:
                  # {"feature": "Dry-Cough", "instances": 2587, "metric_value": 0.8822, "depth": 6}
                  if obj[2]<=0:
                     # {"feature": "Fever", "instances": 2285, "metric_value": 0.7382, "depth": 7}
                     if obj[0]<=0:
                        # {"feature": "Sore-Throat", "instances": 2096, "metric_value": 0.5761, "depth": 8}
                        if obj[4]<=0:
                           # {"feature": "Tiredness", "instances": 1995, "metric_value": 0.4472, "depth": 9}
                           if obj[1]<=0:
                              # {"feature": "Diarrhea", "instances": 1553, "metric_value": 0.3141, "depth": 10}
                              if obj[8]<=0:
                                 return 'no'
                              else:
                                 return 'no'
                           elif obj[1]>0:
                              # {"feature": "Diarrhea", "instances": 442, "metric_value": 0.7633, "depth": 10}
                              if obj[8]<=0:
                                 return 'no'
                              else:
                                 return 'no'
                           else:
                              return 'no'
                        elif obj[4]>0:
                           return 'yes'
                        else:
                           return 'yes'
                     elif obj[0]>0:
                        return 'yes'
                     else:
                        return 'yes'
                  elif obj[2]>0:
                     return 'yes'
                  else:
                     return 'yes'
               elif obj[7]>0:
                  # {"feature": "Sore-Throat", "instances": 1576, "metric_value": 0.1175, "depth": 6}
                  if obj[4]>0:
                     # {"feature": "Tiredness", "instances": 1552, "metric_value": 0.0078, "depth": 7}
                     if obj[1]>0:
                        return 'no'
                     elif obj[1]<=0:
                        return 'yes'
                     else:
                        return 'yes'
                  elif obj[4]<=0:
                     return 'yes'
                  else:
                     return 'yes'
               else:
                  return 'no'
            else:
               return 'no'
         elif obj[3]>0:
            # {"feature": "Pains", "instances": 4068, "metric_value": 0.3643, "depth": 4}
            if obj[5]<=0:
               # {"feature": "Dry-Cough", "instances": 3086, "metric_value": 0.1527, "depth": 5}
               if obj[2]>0:
                  return 'yes'
               elif obj[2]<=0:
                  # {"feature": "Runny-Nose", "instances": 839, "metric_value": 0.4059, "depth": 6}
                  if obj[7]>0:
                     return 'yes'
                  elif obj[7]<=0:
                     # {"feature": "Diarrhea", "instances": 414, "metric_value": 0.6444, "depth": 7}
                     if obj[8]<=0:
                        # {"feature": "Sore-Throat", "instances": 228, "metric_value": 0.8791, "depth": 8}
                        if obj[4]<=0:
                           # {"feature": "Fever", "instances": 142, "metric_value": 0.9987, "depth": 9}
                           if obj[0]<=0:
                              # {"feature": "Tiredness", "instances": 142, "metric_value": 0.9987, "depth": 10}
                              if obj[1]<=0:
                                 return 'yes'
                              else:
                                 return 'yes'
                           else:
                              return 'yes'
                        elif obj[4]>0:
                           return 'yes'
                        else:
                           return 'yes'
                     elif obj[8]>0:
                        return 'yes'
                     else:
                        return 'yes'
                  else:
                     return 'yes'
               else:
                  return 'yes'
            elif obj[5]>0:
               # {"feature": "Diarrhea", "instances": 982, "metric_value": 0.7582, "depth": 5}
               if obj[8]<=0:
                  return 'yes'
               elif obj[8]>0:
                  # {"feature": "Fever", "instances": 225, "metric_value": 0.2623, "depth": 6}
                  if obj[0]>0:
                     # {"feature": "Sore-Throat", "instances": 219, "metric_value": 0.1316, "depth": 7}
                     if obj[4]>0:
                        # {"feature": "Tiredness", "instances": 217, "metric_value": 0.0756, "depth": 8}
                        if obj[1]<=1:
                           # {"feature": "Dry-Cough", "instances": 217, "metric_value": 0.0756, "depth": 9}
                           if obj[2]<=1:
                              # {"feature": "Runny-Nose", "instances": 217, "metric_value": 0.0756, "depth": 10}
                              if obj[7]<=1:
                                 return 'no'
                              else:
                                 return 'no'
                           else:
                              return 'no'
                        else:
                           return 'no'
                     elif obj[4]<=0:
                        return 'yes'
                     else:
                        return 'yes'
                  elif obj[0]<=0:
                     return 'yes'
                  else:
                     return 'yes'
               else:
                  return 'no'
            else:
               return 'yes'
         else:
            return 'yes'
      elif obj[6]>0.0:
         return 'yes'
      else:
         return 'yes'
   elif obj[9]<=0:
      # {"feature": "Nasal-Congestion", "instances": 4757, "metric_value": 0.0119, "depth": 2}
      if obj[6]<=0.0:
         # {"feature": "Difficulty-in-Breathing", "instances": 4754, "metric_value": 0.0053, "depth": 3}
         if obj[3]<=0:
            return 'no'
         elif obj[3]>0:
            # {"feature": "Pains", "instances": 271, "metric_value": 0.0629, "depth": 4}
            if obj[5]>0:
               return 'no'
            elif obj[5]<=0:
               # {"feature": "Sore-Throat", "instances": 55, "metric_value": 0.2254, "depth": 5}
               if obj[4]<=0:
                  return 'no'
               elif obj[4]>0:
                  return 'yes'
               else:
                  return 'yes'
            else:
               return 'no'
         else:
            return 'no'
      elif obj[6]>0.0:
         return 'yes'
      else:
         return 'yes'
   else:
      return 'no'
